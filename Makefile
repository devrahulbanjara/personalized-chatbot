install:
	cd backend && uv venv && . .venv/bin/activate && uv pip install -r requirements.txt
	cd frontend && npm install

run-backend:
	cd backend && . .venv/bin/activate && python -m src.main

run-frontend:
	cd frontend && npm run dev

run-loaddoc-streamlit:
	cd backend && . .venv/bin/activate && python -m src.main & \
	cd backend && . .venv/bin/activate && streamlit run load_documents.py


run-all:
	cd backend && . .venv/bin/activate && python -m src.main & \
	cd frontend && npm run dev

clean:
	rm -rf backend/.venv
	rm -rf frontend/node_modules