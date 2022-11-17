from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Article, ArticleUpdate

router = APIRouter()


@router.post("/", response_description="Create a new article",
             status_code=status.HTTP_201_CREATED, response_model=Article)
def create_article(request: Request, article: Article = Body(...)):
    article = jsonable_encoder(article)
    new_article = request.app.database["articles"].insert_one(article)
    created_article = request.app.database["articles"].find_one(
        {"_id": new_article.inserted_id}
    )

    return created_article


@router.get("/", response_description="List all articles",
            response_model=List[Article])
def list_articles(request: Request):
    articles = list(request.app.database["articles"].find(limit=100))
    return articles


@router.get("/{id}", response_description="Get a single article by id",
            response_model=Article)
def find_article(id: str, request: Request):
    if (article := request.app.database["articles"].find_one({"_id": id})) is not None:
        return article
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Article with ID {id} not found")


@router.put("/{id}", response_description="Update a article",
            response_model=Article)
def update_article(id: str, request: Request, article: ArticleUpdate = Body(...)):
    article = {k: v for k, v in article.dict().items() if v is not None}
    if len(article) >= 1:
        update_result = request.app.database["articles"].update_one(
            {"_id": id}, {"$set": article}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Article with ID {id} not found")

    if (
        existing_article := request.app.database["articles"].find_one({"_id": id})
    ) is not None:
        return existing_article

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Article with ID {id} not found")


@router.delete("/{id}", response_description="Delete a article")
def delete_article(id: str, request: Request, response: Response):
    delete_result = request.app.database["articles"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Article with ID {id} not found")
