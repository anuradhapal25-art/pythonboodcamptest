from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "Python", "author": "John", "available": True},
    {"id": 2, "title": "Java", "author": "David", "available": False},
    {"id": 3, "title": "HTML", "author": "Alex", "available": True}
]


class BookCreate(BaseModel):
    title: str
    author: str
    available: bool


@app.get("/books")
def get_books(available: bool = None):
    if available is not None:
        return [b for b in books if b["available"] == available]
    return books


@app.get("/books/stats")
def get_stats():
    return {
        "total": len(books),
        "available": sum(b["available"] for b in books)
    }


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book: BookCreate):
    for b in books:
        if b["title"] == book.title:
            raise HTTPException(status_code=400, detail="Duplicate title")

    new_book = book.model_dump()
    new_book["id"] = max(b["id"] for b in books) + 1
    books.append(new_book)

    return new_book