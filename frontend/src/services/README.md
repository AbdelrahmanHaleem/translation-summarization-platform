# API Service Documentation

This directory contains the API service that handles communication between the frontend and backend.

## File Structure

- `api.ts` - Main API service file containing all backend communication logic

## API Endpoints

### Translation Service
- Endpoint: `/translate/{direction}`
- Method: `POST`
- Directions: 
  - `ar2en`: Arabic to English
  - `en2ar`: English to Arabic
- Request Body:
  ```typescript
  {
    text: string
  }
  ```
- Response:
  ```typescript
  {
    translated_text: string
  }
  ```

### Summarization Service
- Endpoint: `/summarize`
- Method: `POST`
- Request Body:
  ```typescript
  {
    text: string
  }
  ```
- Response:
  ```typescript
  {
    summary: string
  }
  ```

### Health Check
- Endpoint: `/health`
- Method: `GET`
- Response:
  ```typescript
  {
    status: "healthy" | "error",
    message: string
  }
  ```

## Error Handling

The service includes comprehensive error handling for:
- Server connection issues
- Request timeouts (30 seconds)
- Invalid responses
- Network errors

## Usage Example

```typescript
import { translateText, summarizeText } from './api';

// Translation
try {
  const result = await translateText("Hello world", "en2ar");
  console.log(result.translated_text);
} catch (error) {
  console.error("Translation failed:", error);
}

// Summarization
try {
  const result = await summarizeText("Long text to summarize...");
  console.log(result.summary);
} catch (error) {
  console.error("Summarization failed:", error);
}
```
