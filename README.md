# Company Specialized Chatbot

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Groq-black?style=for-the-badge&logo=google-cloud&logoColor=white)](https://groq.com/)
[![Llama 3](https://img.shields.io/badge/Llama_3-black?style=for-the-badge&logo=meta&logoColor=white)](https://llama.meta.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)

This is a sophisticated, personalized chatbot application powered by a FastAPI backend and a modern React frontend. It features a clean, responsive user interface with voice-to-text capabilities and is designed to provide intelligent, context-aware responses based on a knowledge base of your choice, with ultra-low latency thanks to the Groq LPU™ Inference Engine.

## Features

- **Modern UI**: A beautiful and responsive chat interface built with React, TypeScript, and Shadcn/UI.
- **Voice-to-Text**: Integrated speech recognition for hands-free interaction using the Web Speech API.
- **RAG-based Architecture**: The backend utilizes a Retrieval-Augmented Generation (RAG) approach to provide answers from a custom knowledge base.
- **High-Performance Backend**: Built with FastAPI, ensuring high speed and efficiency.
- **Asynchronous by Design**: Leverages Python's async capabilities for non-blocking API endpoints.
- **Clear Project Structure**: A clean separation between the frontend and backend concerns for better maintainability.

## Tech Stack

| Area         | Technology                                                                                         |
| :----------- | :------------------------------------------------------------------------------------------------- |
| **Frontend** | React, TypeScript, Vite, Tailwind CSS, Shadcn/UI, Lucide React (icons), `react-speech-recognition` |
| **Backend**  | Python, FastAPI, Uvicorn, Pydantic, Groq (for Llama 3 LLM), PyMuPDF (for document parsing)         |
| **Tooling**  | `npm` for frontend package management, `uv` for Python package management, `Make` for automation   |

## Project Structure

```
.
├── backend/
│   ├── src/
│   │   ├── main.py             # FastAPI application entrypoint and middleware
│   │   ├── orchestration.py    # Core logic for RAG (retrieve, generate response)
│   │   └── routes/             # API route definitions
│   ├── pyproject.toml        # Backend dependencies (for uv)
│   └── requirements.txt      # Alternative dependency file
└── frontend/
    ├── src/
    │   ├── main.tsx            # React application entrypoint
    │   ├── App.tsx             # Main App component and router setup
    │   ├── pages/
    │   │   └── Index.tsx       # The main chat interface component
    │   ├── components/         # Reusable UI components (Shadcn/UI)
    │   └── lib/                # Utility functions
    ├── package.json          # Frontend dependencies and scripts
    └── vite.config.ts        # Vite configuration
└── Makefile                # Automation scripts for installation, running, etc.
```

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- [Node.js](https://nodejs.org/) (v18 or later)
- [Python](https://www.python.org/downloads/) (v3.10 or later)
- `uv` (Python package installer from Astral). If you don't have it, run:
  ```bash
  curl -Ls https://astral.sh/uv/install.sh | sh
  ```
- `make` utility (usually pre-installed on Linux and macOS).

### Option 1: Using Make (Recommended)

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/devrahulbanjara/personalized-chatbot
    cd personalized-chatbot
    ```

2.  **Install all dependencies:**
    This single command will set up the backend virtual environment and install all Python and Node.js packages.

    ```bash
    make install
    ```

3.  **Run the application:**
    For the best development experience, run the backend and frontend in separate terminals.

    In your first terminal:

    ```bash
    make run-backend
    ```

    In your second terminal:

    ```bash
    make run-frontend
    ```

### Option 2: Manual Installation

If you prefer not to use `make`, you can follow these steps.

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd personalized-chatbot
    ```

2.  **Setup the Backend:**
    Navigate to the backend directory, create a virtual environment, and install the dependencies.

    ```bash
    cd backend
    uv venv         # Create virtual environment
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    uv pip install -r requirements.txt
    ```

3.  **Setup the Frontend:**
    In a separate terminal, navigate to the frontend directory and install the dependencies.
    ```bash
    cd frontend
    npm install
    ```

### Running the Application

1.  **Start the Backend Server:**
    From the `backend` directory (with the virtual environment activated):

    ```bash
    uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
    ```

    The API will be available at `http://localhost:8000`.

2.  **Start the Frontend Development Server:**
    From the `frontend` directory:
    ```bash
    npm run dev
    ```
    The application will be accessible at `http://localhost:5173` (or another port if 5173 is busy).

## API Endpoints

The backend exposes the following main endpoints:

- `POST /api/chat`: The main endpoint for sending a user query and receiving a response from the chatbot.
- `GET /`: A root endpoint to welcome you to the API.
- `GET /docs`: Access the interactive Swagger UI for API documentation.

## Makefile Commands

The `Makefile` provides several commands to streamline development:

- `make install`: Installs all dependencies for both frontend and backend.
- `make run-backend`: Starts the backend server.
- `make run-frontend`: Starts the frontend development server.
- `make clean`: Removes all installed dependencies and virtual environments.
- `make help`: Displays a list of all available commands.

## Contributing

Contributions are welcome! Please feel free to open a pull request or submit an issue.

1.  Fork the repository
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---
