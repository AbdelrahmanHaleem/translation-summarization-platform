from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import BartForConditionalGeneration, BartTokenizer
from fastapi import FastAPI, HTTPException
import logging
import time

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "HEAD", "OPTIONS"],
        "allow_headers": ["Content-Type", "Accept"]
    }
})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Model configuration
MODEL_NAME = "facebook/bart-large-cnn"
model = None
tokenizer = None

def load_model():
    global model, tokenizer
    try:
        logger.info("Loading summarization model and tokenizer...")
        start_time = time.time()
        model = BartForConditionalGeneration.from_pretrained(MODEL_NAME)
        tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
        end_time = time.time()
        logger.info(f"Summarization model loaded successfully in {end_time - start_time:.2f} seconds")
    except Exception as e:
        logger.error(f"Error loading summarization model: {str(e)}")
        return False
    return True


@app.route("/health", methods=["GET", "HEAD"])
def health_check():
    if model is None or tokenizer is None:
        return jsonify({"status": "error", "message": "Model or tokenizer not loaded"}), 503
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

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
            max_length=300,
            length_penalty=2.0,
            early_stopping=True
        )
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        logger.info(f"Summarization successful. Result: {summary[:100]}...")
        return jsonify({"summary": summary})

    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        return jsonify({"error": f"Summarization failed: {str(e)}"}), 500

@app.route("/summarize/status/<id>", methods=["GET"])
def get_status(id):
    return jsonify({"status": "In Progress", "request_id": id})


if __name__ == "__main__":
    if load_model():
        logger.info("Starting server...")
        app.run(host="0.0.0.0", port=7002, debug=True)
    else:
        logger.error("Failed to load model. Exiting...")
        exit(1)
