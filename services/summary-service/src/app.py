from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load the summarization model
summarizer = pipeline("summarization")

class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str

@app.post("/summarize", response_model=SummarizationResponse)
async def summarize(request: SummarizationRequest):
    try:
        # Summarize the text
        summary = summarizer(request.text, max_length=150, min_length=50, do_sample=False)
        return SummarizationResponse(summary=summary[0]['summary_text'])
    except Exception as e:
        raise HTTPException(status_code=500, detail="Summarization failed")

@app.get("/summarize/status/{id}")
async def get_status(id: str):
    # In a real implementation, you would query the status of the task.
    return {"status": "In Progress", "request_id": id}

