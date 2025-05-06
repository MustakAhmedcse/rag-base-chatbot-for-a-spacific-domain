import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag_pipeline import rag_pipeline
from app.utils import is_bangla

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question.strip()
    logging.info(f"Received question: {question}")
    if not question:
        logging.warning("Question is empty.")
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    language = "Bangla" if is_bangla(question) else "English"
    logging.info(f"Detected language: {language}")
    try:
        answer = rag_pipeline.get_response(question, language)
        logging.info(f"Generated answer: {answer}")
    except Exception as e:
        logging.error(f"Error processing question: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing question: {str(e)}")
    return {"question": question, "answer": answer, "language": language}
