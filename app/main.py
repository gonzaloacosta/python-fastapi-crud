from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as article_router


config = dotenv_values(".env")


app = FastAPI()


@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["DB_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Disconnected to the MongoDB database!")


app.include_router(article_router, tags=["article"], prefix="/article")
