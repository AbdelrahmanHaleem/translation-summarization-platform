from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import (
    MarianMTModel, 
    MarianTokenizer,
    BartForConditionalGeneration, 
    BartTokenizer
)
import logging
import time

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],  # Allow requests from React dev server
        "methods": ["GET", "POST", "HEAD", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"]
    }
})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Model configurations
MODELS = {
    'ar2en': {
        'name': "Helsinki-NLP/opus-mt-ar-en",
        'model': None,
        'tokenizer': None,
        'type': 'translation'
    },
    'en2ar': {
        'name': "Helsinki-NLP/opus-mt-en-ar",
        'model': None,
        'tokenizer': None,
        'type': 'translation'
    },
    'summarize': {
        'name': "facebook/bart-large-cnn",
        'model': None,
        'tokenizer': None,
        'type': 'summarization'
    }
}

def load_models():
    success = True
    for model_key, config in MODELS.items():
        try:
            logger.info(f"Loading {model_key} model and tokenizer...")
            start_time = time.time()
            
            if config['type'] == 'translation':
                config['model'] = MarianMTModel.from_pretrained(config['name'])
                config['tokenizer'] = MarianTokenizer.from_pretrained(config['name'])
            else:  # summarization
                config['model'] = BartForConditionalGeneration.from_pretrained(config['name'])
                config['tokenizer'] = BartTokenizer.from_pretrained(config['name'])
                
            end_time = time.time()
            logger.info(f"{model_key} model loaded successfully in {end_time - start_time:.2f} seconds")
        except Exception as e:
            logger.error(f"Error loading {model_key} model: {str(e)}")
            success = False
    return success

@app.route("/health", methods=["GET", "HEAD"])
def health_check():
    all_models_loaded = all(config['model'] is not None and config['tokenizer'] is not None 
                          for config in MODELS.values())
    if not all_models_loaded:
        return jsonify({"status": "error", "message": "Some models not loaded"}), 503
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

@app.route("/translate/<direction>", methods=["POST", "HEAD", "OPTIONS"])
def translate(direction):
    if request.method == "HEAD" or request.method == "OPTIONS":
        return "", 200
        
    if direction not in MODELS or MODELS[direction]['type'] != 'translation':
        return jsonify({"error": f"Invalid translation direction. Use one of: {[k for k, v in MODELS.items() if v['type'] == 'translation']}"}), 400
        
    if MODELS[direction]['model'] is None or MODELS[direction]['tokenizer'] is None:
        return jsonify({"error": "Model not loaded. Please try again later."}), 503

    try:
        data = request.get_json()
        if not data:
            logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400

        text = data.get('text')
        if not text:
            logger.error("No text field in JSON data")
            return jsonify({"error": "No text provided"}), 400
        
        logger.info(f"Received text for {direction} translation: {text[:100]}...")
        
        # Translate the text
        model = MODELS[direction]['model']
        tokenizer = MODELS[direction]['tokenizer']
        
        tokens = tokenizer(text, return_tensors="pt", padding=True)
        translated_tokens = model.generate(**tokens)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        logger.info(f"Translation successful. Result: {translated_text[:100]}...")
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500

@app.route("/summarize", methods=["POST", "HEAD", "OPTIONS"])
def summarize():
    if request.method == "HEAD" or request.method == "OPTIONS":
        return "", 200
        
    model_config = MODELS['summarize']
    if model_config['model'] is None or model_config['tokenizer'] is None:
        return jsonify({"error": "Summarization model not loaded. Please try again later."}), 503

    try:
        data = request.get_json()
        if not data:
            logger.error("No JSON data received")
            return jsonify({"error": "No data provided"}), 400

        text = data.get('text')
        if not text:
            logger.error("No text field in JSON data")
            return jsonify({"error": "No text provided"}), 400
        
        logger.info(f"Received text for summarization: {text[:100]}...")
        
        # Summarize the text
        model = model_config['model']
        tokenizer = model_config['tokenizer']
        
        inputs = tokenizer(text, max_length=1024, truncation=True, return_tensors="pt")
        summary_ids = model.generate(
            inputs["input_ids"], 
            num_beams=4,
            min_length=30,
            max_length=150,
            length_penalty=2.0,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        logger.info(f"Summarization successful. Result: {summary[:100]}...")
        return jsonify({"summary": summary})

    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        return jsonify({"error": f"Summarization failed: {str(e)}"}), 500

@app.route("/translate/ar2en/status/<id>", methods=["GET"])
def get_status(id):
    return jsonify({"status": "In Progress", "request_id": id})

if __name__ == "__main__":
    if load_models():
        logger.info("Starting server...")
        app.run(host="0.0.0.0", port=8000, debug=True)
    else:
        logger.error("Failed to load models. Exiting...")
        exit(1)
