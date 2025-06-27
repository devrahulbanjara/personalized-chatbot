# Personalized Chatbot 🤖

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-00897B?style=for-the-badge&logo=database&logoColor=white)](https://www.trychroma.com/)
[![uv](https://img.shields.io/badge/uv-Package%20Installer-blueviolet?style=for-the-badge)](https://github.com/astral-sh/uv)

A powerful personalized chatbot system that can be trained on your custom documents. Built with modern Python stack, featuring a FastAPI backend and a Streamlit frontend, powered by Google Gemini's advanced language model.

## 📁 Project Structure

```
personalized-chatbot/
├── app.py                 # Main Streamlit chat interface
├── data/                  # Data storage directory
├── database/             # Database related modules
│   ├── chromadb_file/    # ChromaDB storage
│   ├── database.py       # Database operations
│   ├── document_store.py # Document storage logic
│   └── vector_store.py   # Vector store operations
├── load_documents.py     # Document loading interface
├── models/              # Model definitions
├── parser/             # Document parsing utilities
├── prompts/            # Chatbot prompt templates
├── src/               # Core application source
│   ├── main.py        # FastAPI application
│   ├── orchestration.py # Service orchestration
│   └── routes/        # API routes
└── requirements.txt    # Project dependencies
```

## 🚀 Features

- 📚 Document ingestion and processing
- 🔍 Vector-based document search using ChromaDB
- 💬 Interactive chat interface
- 🎯 Context-aware responses using Google Gemini
- 🔒 Secure API endpoints
- 🌐 Modern web interface

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Frontend**: Streamlit
- **Language Model**: Google Gemini
- **Database**: ChromaDB (Vector Store)
- **Package Management**: uv
- **Document Processing**: PyMuPDF
- **API Documentation**: Swagger UI (via FastAPI)
- **Dependency Management**: uv + requirements.txt

## 📋 Prerequisites

- Python 3.10+
- uv package installer
- Make (for using Makefile commands)

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/devrahulbanjara/personalized-chatbot.git
   cd personalized-chatbot
   ```

2. Install uv (if not already installed):

   ```bash
   curl -Ls https://astral.sh/uv/install.sh | sh
   ```

3. Set up environment and install dependencies:

   ```bash
   make install
   ```

4. Create a `.env` file in the root directory:

   ```bash
   # Copy and modify with your API keys and configurations
   touch .env
   ```

   Required environment variables:

   ```env
   # Add your API keys and configurations here
   GEMINI_API_KEY=your_api_key_here
   # Add other required environment variables
   ```

## 🚀 Running the Application

### Running Components Separately

1. Start the document loading frontend:

   ```bash
   make run-loaddoc-streamlit
   ```

2. Start the backend server:
   ```bash
   make run-backend
   ```

### Running Everything Together

To start both frontend and backend simultaneously:

```bash
make run-all
```

## 🌐 Accessing the Application

- Frontend (Chat Interface): http://localhost:8501
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 🧹 Cleanup

To clean up the virtual environment:

```bash
make clean
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments

- FastAPI for the amazing web framework
- Streamlit for the intuitive UI components
- Google Gemini for the powerful language model
- ChromaDB for vector storage capabilities
- All other open-source contributors
