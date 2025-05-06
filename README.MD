# Banglalink Retailer App RAG Chatbot

## Project Structure

```
rag-code-new/
│
├── app/
│   ├── __init__.py
│   ├── api.py              # FastAPI endpoints (chatbot)
│   ├── main.py             # FastAPI app entrypoint
│   ├── rag_pipeline.py     # RAG pipeline logic
│   ├── llm_config.py       # LLM config and initialization
│   ├── utils.py            # Utility functions
│   └── manual_upload.py    # Manual upload & vector DB processing
│
├── chroma_db/              # Vector DB files
├── uploaded_manuals/       # Uploaded files (only latest .txt manual)
├── requirements.txt
├── README.MD
├── user_manual.txt         # Example manual
└── ...
```

## Features
- Answers any question about the Banglalink Retailer App as described in the user manual.
- Only the latest .txt manual is accepted and processed (previous uploads are deleted).
- Provides step-by-step guidance for all app features, sections, and usage.
- Uses FastAPI for API endpoints: `/ask` (chatbot) and `/upload_manual` (manual upload).
- Utilizes LangGraph and a RAG pipeline to retrieve information from the manual and generate responses.
- Logs every step in a human-readable format for easy debugging and tracking.

## Requirements
- **Python 3.8+**
- **Ollama Server** (if using Ollama LLM) or OpenAI API key (if using OpenAI)
- **Dependencies**: See `requirements.txt`

## Setup & Usage

1. **Create and activate a virtual environment**
   ```bash
   python -m venv rag_env
   .\rag_env\Scripts\activate  # On Windows
   # or
   source rag_env/bin/activate  # On Linux/Mac
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **(If using Ollama) Start the Ollama server and pull the model**
   ```bash
   ollama serve
   ollama pull llama3
   ```

4. **Run the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Upload the user manual (.txt only, one at a time)**
   - The previous manual will be deleted before each upload.
   - Example (using curl):
     ```bash
     curl -F "file=@user_manual.txt" http://localhost:8000/upload_manual
     ```
   - Only .txt files are accepted.

6. **Ask a question about the app**
   - POST to `/ask` with JSON body `{ "question": "your question here" }`
   - Example (using curl):
     ```bash
     curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question": "How can I see my SIM Sales data?"}'
     ```

7. **API Documentation**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Notes
- All logic is modularized in the `app/` package.
- Only the latest uploaded .txt manual is used for answering questions.
- All logs are printed in a human-readable format in the terminal.
- For custom logic or tests, add new modules under `app/` or a `tests/` folder.

## Troubleshooting
- **500 Internal Server Error on upload:** Ensure you are uploading a valid .txt file and the file is UTF-8 encoded.
- **No answer or unclear answer:** Make sure the manual is uploaded and contains the relevant information.
- **Bangla/English detection:** The bot will auto-detect and respond in the appropriate language if the manual contains both.

## License
This project is licensed under the MIT License.