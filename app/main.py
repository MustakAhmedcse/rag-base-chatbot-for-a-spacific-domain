import logging
from fastapi import FastAPI
from app.api import router as api_router
from app.manual_upload import router as manual_upload_router

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Starting FastAPI application...")

app = FastAPI()

# Include routers
app.include_router(api_router)
logging.info("API router included.")
app.include_router(manual_upload_router)
logging.info("Manual upload router included.")

# Run the app with: uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    logging.info("Running app with Uvicorn...")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
