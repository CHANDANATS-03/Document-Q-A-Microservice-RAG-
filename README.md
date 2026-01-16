Document Q&A Microservice (RAG)
1. Project Overview and Selected Task

The selected task for this assignment is Task 1 — Document Q&A Microservice (RAG).
This project implements a backend service that enables users to upload PDF documents and ask natural language questions about their content. The system follows a Retrieval-Augmented Generation (RAG) approach, where relevant sections of the document are retrieved using vector similarity search and then used to generate accurate answers. The solution demonstrates document ingestion, embedding generation, vector database usage, and question answering using a language model.

2. Architecture Summary

The system is designed as a modular backend service. When a user uploads a document, the backend extracts text from the PDF, splits the text into manageable chunks, and generates vector embeddings for each chunk. These embeddings are stored in a vector database for efficient similarity search. When a user submits a question, the system converts the question into an embedding, retrieves the most relevant document chunks from the vector database, and uses those chunks as context to generate a final answer using a language model. Metadata such as document name and upload time is stored separately in a lightweight database.

3. Setup Instructions
Python Version

The project requires Python version 3.9 or higher.

Environment Creation

A virtual environment is created to isolate project dependencies from the system Python environment. This ensures consistent behavior across different systems and avoids dependency conflicts.

Dependency Installation

All required Python libraries are installed using a requirements file that lists the backend framework, embedding models, vector database libraries, PDF processing tools, and optional UI dependencies.

How to Run the API

The backend API is started using a FastAPI ASGI server. Once running, the API listens on a local port and exposes endpoints for health checks, document uploads, and question answering.

How to Test Endpoints (curl / Postman)

The API can be tested using tools such as curl or Postman. A health check endpoint confirms that the service is running. The document upload endpoint allows users to submit a PDF file, and the query endpoint accepts a natural language question to retrieve and generate an answer from the uploaded document.

4. Optional Streamlit UI Setup

An optional Streamlit-based user interface is provided for easier interaction with the system. The UI allows users to upload PDF files and ask questions through a web interface instead of using API tools. This component is optional and not required for core backend functionality.

5. Environment Variables Explanation

The project uses environment variables to manage sensitive configuration values. These variables are stored in a separate environment file and loaded at runtime. An API key is required when using a hosted language model service for answer generation. This approach keeps sensitive information out of the source code and supports secure configuration management.

6. Notes and Assumptions

The system is designed for small to medium-sized documents and uses local vector storage for simplicity. Chunk size and overlap are configurable and chosen to balance retrieval accuracy and performance. FAISS is used in CPU mode, and SQLite is used for lightweight metadata storage. The focus of this project is on demonstrating a clear and correct RAG pipeline rather than optimizing for large-scale production deployment.
