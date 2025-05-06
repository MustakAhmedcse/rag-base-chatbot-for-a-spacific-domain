import logging
from app.llm_config import llm_config
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END
from typing import Dict, Any

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class RAGPipeline:
    def __init__(self, llm_config):
        logging.info("Initializing RAGPipeline...")
        embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
        logging.info("Chroma vectorstore initialized.")
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})
        logging.info("Retriever initialized.")
        prompt_template = """
        You are a helpful assistant for the Banglalink Retailer App. You have access to the full user guideline and manual below. Answer any user question about the app's features, sections, or usage as described in the manual. Provide clear, step-by-step guidance in {language}. If the question is not covered in the manual, respond with: \"I can only assist with questions related to the Banglalink Retailer App as described in the user manual. Please ask a relevant question.\" If the question is unclear or no relevant context is found, ask for clarification.

        Context (from the user manual): {context}

        Question: {question}

        Answer:
        """
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question", "language"]
        )
        self.rag_chain = (
            {
                "context": lambda x: "\n".join(doc.page_content for doc in self.retriever.invoke(x["question"])),
                "question": lambda x: x["question"],
                "language": lambda x: x["language"]
            }
            | prompt
            | llm_config.llm
            | StrOutputParser()
        )
        logging.info("RAG chain initialized.")
        class ChatbotState(Dict[str, Any]):
            question: str
            language: str
            answer: str
            needs_clarification: bool
        def chatbot_node(state: ChatbotState) -> ChatbotState:
            logging.info(f"Processing question in chatbot_node: {state['question']}")
            # Remove strict relevance check, always try to answer from manual
            context = self.retriever.invoke(state["question"])
            logging.info(f"Retrieved {len(context)} context documents.")
            if not context:
                state["answer"] = f"No relevant information found in {state['language']}. Please clarify your question."
                state["needs_clarification"] = True
                logging.info("No relevant context found.")
                return state
            answer = self.rag_chain.invoke({"question": state["question"], "language": state["language"]})
            state["answer"] = answer.strip()
            state["needs_clarification"] = False
            logging.info(f"Answer generated: {state['answer']}")
            return state
        workflow = StateGraph(ChatbotState)
        workflow.add_node("chatbot", chatbot_node)
        workflow.set_entry_point("chatbot")
        workflow.add_edge("chatbot", END)
        self.app = workflow.compile()
        logging.info("RAGPipeline workflow compiled.")
    def get_response(self, question: str, language: str) -> str:
        logging.info(f"Invoking RAGPipeline for question: {question}")
        result = self.app.invoke({"question": question, "language": language, "answer": "", "needs_clarification": False})
        logging.info(f"RAGPipeline result: {result['answer']}")
        return result["answer"]

rag_pipeline = RAGPipeline(llm_config)
