install:
	uv venv
	. .venv/bin/activate && uv pip install -r requirements.txt
		
run-loaddoc-streamlit:
	. .venv/bin/activate && streamlit run load_documents.py

run-backend:
	. .venv/bin/activate && python -m src.main

run-all:
	. .venv/bin/activate && streamlit run app.py &
	. .venv/bin/activate && python -m src.main

clean:
	rm -rf .venv
