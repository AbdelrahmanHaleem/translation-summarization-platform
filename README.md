# Translation and Summarization Platform

A powerful web application that provides translation services between Arabic and English, along with text summarization capabilities. Built with React, TypeScript, and Python Flask, utilizing state-of-the-art machine learning models from Hugging Face.

## Features

- **Bidirectional Translation:**
  - Arabic to English translation
  - English to Arabic translation
  - Real-time translation with error handling

- **Text Summarization:**
  - Powered by Facebook's BART-large-CNN model
  - Configurable summary length and quality
  - Optimized for English text

- **Modern UI/UX:**
  - React-based frontend with TypeScript
  - Material-UI components
  - Responsive design
  - Loading indicators and error feedback

## System Requirements

### Backend Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)
- 4GB RAM minimum (8GB recommended for better performance)
- 10GB free disk space (for models and dependencies)

### Frontend Requirements
- Node.js 14.x or higher
- npm 6.x or higher
- Modern web browser (Chrome, Firefox, Safari, or Edge)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/translation-summarization-platform.git
cd translation-summarization-platform
```

### 2. Backend Setup
1. Install Python dependencies:
```bash
# Install Python if not already installed
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Create and activate virtual environment
cd services/ar2en-service
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

2. Start the backend server:
```bash
python3 src/app.py
```
The server will run on `http://localhost:8000`

### 3. Frontend Setup
1. Install Node.js and npm if not already installed:
```bash
# Using Ubuntu
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version
npm --version
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Start the development server:
```bash
npm start
```
The frontend will run on `http://localhost:3000`

## Tech Stack

### Frontend
- React with TypeScript
- Material-UI for components
- Fetch API for HTTP requests
- Error handling and logging

### Backend
- Flask web framework
- Flask-CORS for cross-origin support
- Hugging Face Transformers
- PyTorch
- Logging and error handling

## Models Used

- **Translation:** Helsinki-NLP's MarianMT models
  - Arabic to English: `Helsinki-NLP/opus-mt-ar-en`
  - English to Arabic: `Helsinki-NLP/opus-mt-en-ar`
- **Summarization:** Facebook's BART model
  - `facebook/bart-large-cnn`

## Project Structure

```
translation-summarization-platform/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── pages/          # Page components
│   │   ├── services/       # API services
│   │   └── components/     # Reusable components
│   └── package.json
└── services/
    └── ar2en-service/      # Translation and summarization service
        ├── src/
        │   └── app.py      # Flask application
        └── requirements.txt # Python dependencies
```

## API Endpoints

- `GET /health` - Health check endpoint
- `POST /translate/ar2en` - Arabic to English translation
- `POST /translate/en2ar` - English to Arabic translation
- `POST /summarize` - Text summarization

## Error Handling

The application includes comprehensive error handling:
- Connection issues
- Model loading failures
- Invalid input
- Timeouts
- CORS issues

## Logging

Both frontend and backend include detailed logging:
- Request/response logging
- Error logging
- Model loading status
- Translation and summarization progress

## Troubleshooting

### Common Issues

1. **Backend won't start:**
   - Ensure Python 3.8+ is installed
   - Check virtual environment is activated
   - Verify all dependencies are installed
   - Check for port conflicts on 8000

2. **Frontend won't start:**
   - Ensure Node.js is properly installed
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules and reinstall: 
     ```bash
     rm -rf node_modules
     npm install
     ```

3. **Models fail to load:**
   - Ensure enough disk space
   - Check internet connection (needed for first-time model download)
   - Increase available RAM

4. **CORS errors:**
   - Verify backend is running on port 8000
   - Check CORS configuration in backend
   - Ensure frontend is running on port 3000

### Getting Help

If you encounter issues:
1. Check the logs in both frontend and backend terminals
2. Verify all installation steps were followed
3. Ensure system requirements are met
4. Create an issue in the GitHub repository

## Future Improvements

- Add support for more language pairs
- Implement caching for frequent translations
- Add user authentication
- Add rate limiting
- Implement batch processing for large texts
- Add support for file uploads
