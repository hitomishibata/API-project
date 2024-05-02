import requests
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from enum import Enum
from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    EN = "en"
    ES = "es"
    FR = "fr"
    IT = "it"
    PT = "pt"

class Item (BaseModel):
    artifact: str
    category: Category

class Book (BaseModel):
    title: str
    originalTitle: str
    releaseDate: str
    description: str
    pages: int
    cover: str


items = {
    0: Item(artifact="books", category=Category.EN),
    1: Item(artifact="characters", category=Category.EN),
    2: Item(artifact="houses", category=Category.EN),
    3: Item(artifact="spells", category=Category.EN),
    4: Item(artifact="books", category=Category.ES),
}

books = {
    0: Book(title="Harry Potter and the Sorcerer's Stone",
            originalTitle="Harry Potter and the Sorcerer's Stone",
            releaseDate="Jun 26, 1997",
            description= "On his birthday, Harry Potter discovers that he is the son of two well-known wizards, from whom he has inherited magical powers. He must attend a famous school of magic and sorcery, where he establishes a friendship with two young men who will become his companions on his adventure. During his first year at Hogwarts, he discovers that a malevolent and powerful wizard named Voldemort is in search of a philosopher's stone that prolongs the life of its owner.",
            pages= 223,
            cover= "https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/covers/1.png"),
    1: Book(title="Harry Potter and the chamber of secrets",
            originalTitle="Harry Potter and the chamber of secrets",
            releaseDate="Jul 2, 1998",
            description="Harry Potter and the sophomores investigate a malevolent threat to their Hogwarts classmates, a menacing beast that hides within the castle.",
            pages=251,
            cover="https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/covers/2.png"),
    2: Book(title= "Harry Potter and the Prisoner of Azkaban",
            originalTitle="Harry Potter and the Prisoner of Azkaban",
            releaseDate="Jul 8, 1999",
            description="Harry's third year of studies at Hogwarts is threatened by Sirius Black's escape from Azkaban prison. Apparently, it is a dangerous wizard who was an accomplice of Lord Voldemort and who will try to take revenge on Harry Potter.",
            pages=317,
            cover="https://raw.githubusercontent.com/fedeperin/potterapi/main/public/images/covers/3.png"),

}

@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items":items}
    
#present the data of each item
@app.get("/items/{item_id}")
def view_item(item_id:int, q: str|None = None) -> Item:
     if item_id not in items:
         raise HTTPException(
             status_code=404, details=f"Item with {item_id} does not exist."
         )
     else: 
        if item_id == 0:
            return books
        else:
            print("the data is not uploaded yet.")
            

@app.get("/items/{item_id}/{book_id}")
def view_book(book_id:int, q: str|None = None) -> Book:
    if book_id not in books:
        raise HTTPException(
            status_code=404, details=f"Book with {book_id} does not exist."
        )
    else:
        return books[book_id]

@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")
    else:
        items[item.id] = item
        return {"added": item}

@app.put("en/0/update/{book_id}")
def update_item(book_id:int) -> Book:
    if book_id not in books:
        raise HTTPException(
             status_code=404, details=f"Book with {book_id} does not exist."
         )
    else:
        book = books[book_id]
        return {books: book}
    
