git clone <repo-url> personal-chatbot
cd personal-chatbot

curl -Ls https://astral.sh/uv/install.sh | sh   # install uv, if needed

uv venv
source .venv/bin/activate

uv pip install -r requirements.txt

run-loaddoc-streamlit to run the forntend for loading document
make run-backend to run backend separately

make run-all to run frontend and backend to inference the chatbot

