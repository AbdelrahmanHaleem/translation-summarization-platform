from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

app = FastAPI()

# Load the model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-ar"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

class TranslationRequest(BaseModel):
    text: str

class TranslationResponse(BaseModel):
    translated_text: str

@app.post("/translate/en2ar", response_model=TranslationResponse)
async def translate(request: TranslationRequest):
    try:
        # Translate the text
        tokens = tokenizer(request.text, return_tensors="pt", padding=True)
        translated_tokens = model.generate(**tokens)
        translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return TranslationResponse(translated_text=translated_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Translation failed")

@app.get("/translate/en2ar/status/{id}")
async def get_status(id: str):
    # In a real implementation, you would query the status of the task.
    return {"status": "In Progress", "request_id": id}

