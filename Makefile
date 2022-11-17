venv:
	@python -m venv venv-pymongo-fastapi-crud

init:
	@pip install -r requirements.txt

run:
	@cd app && python -m uvicorn main:app --reload

build:
	@sudo docker build -t gonzaloacosta/pymongo-fastapi-crud:latest .

push:
	@sudo docker push gonzaloacostea/pymongo-fastapi-crud:latest
