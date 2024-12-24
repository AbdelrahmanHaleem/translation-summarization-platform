# Translation and Summarization Backend Service

This service provides the backend API for translation and summarization functionality.

## Features

- Bidirectional translation (Arabic ↔ English)
- Text summarization
- Health check endpoint
- CORS support
- Comprehensive error handling
- Detailed logging

## Models Used

### Translation Models
- Arabic to English: `Helsinki-NLP/opus-mt-ar-en`
- English to Arabic: `Helsinki-NLP/opus-mt-en-ar`

### Summarization Model
- Facebook BART: `facebook/bart-large-cnn`

## API Endpoints

### Health Check
```
GET /health
Response: {
    "status": "healthy" | "error",
    "message": string
}
```

### Translation
```
POST /translate/{direction}
direction: "ar2en" | "en2ar"
Request Body: {
    "text": string
}
Response: {
    "translated_text": string
}
```

### Summarization
```
POST /summarize
Request Body: {
    "text": string
}
Response: {
    "summary": string
}
```

## Setup

1. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python3 src/app.py
```

## Dependencies

See `requirements.txt` for full list. Key dependencies:
- Flask
- Flask-CORS
- Transformers
- PyTorch
- SentencePiece

## Configuration

- Server runs on port 8000
- CORS configured for frontend origin (http://localhost:3000)
- Model configurations in `app.py`
- Logging level: INFO

## Error Handling

The service handles:
- Invalid input
- Model loading failures
- Translation/summarization errors
- Connection issues
- CORS errors

## Logging

Comprehensive logging for:
- Server startup
- Model loading
- Request processing
- Error states
- Response details

## System Requirements

- Python 3.8+
- 8GB RAM recommended
- 10GB disk space
- CUDA-capable GPU (optional, for better performance)
