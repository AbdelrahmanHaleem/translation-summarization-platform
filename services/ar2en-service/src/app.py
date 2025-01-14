from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import MarianMTModel, MarianTokenizer
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
MODEL_NAME = "Helsinki-NLP/opus-mt-ar-en"
model = None
tokenizer = None

def load_model():
    global model, tokenizer
    try:
        logger.info("Loading ar2en model and tokenizer...")
        start_time = time.time()
        model = MarianMTModel.from_pretrained(MODEL_NAME)
        tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
        end_time = time.time()
        logger.info(f"ar2en model loaded successfully in {end_time - start_time:.2f} seconds")
    except Exception as e:
        logger.error(f"Error loading ar2en model: {str(e)}")
        return False
    return True


@app.route("/health", methods=["GET", "HEAD"])
def health_check():
    if model is None or tokenizer is None:
        return jsonify({"status": "error", "message": "Model or tokenizer not loaded"}), 503
    return jsonify({"status": "healthy", "message": "Service is running"}), 200

@app.route("/translate/ar2en", methods=["POST", "HEAD", "OPTIONS"])
def translate_ar2en():
    if request.method == "HEAD" or request.method == "OPTIONS":
        return "", 200

    if model is None or tokenizer is None:
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

        logger.info(f"Received text for ar2en translation: {text[:100]}...")
        tokens = tokenizer(text, return_tensors="pt", padding=True)
        translated_tokens = model.generate(**tokens)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        logger.info(f"Translation successful. Result: {translated_text[:100]}...")
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        logger.error(f"Translation error: {str(e)}")
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500

@app.route("/translate/ar2en/status/<id>", methods=["GET"])
def get_status(id):
    return jsonify({"status": "In Progress", "request_id": id})

if __name__ == "__main__":
    if load_model():
        logger.info("Starting server...")
        app.run(host="0.0.0.0", port=8000, debug=True)
    else:
        logger.error("Failed to load model. Exiting...")
        exit(1)
