import requests
import pandas as pd

def put_book_to_specific_id(fields):
    book_id = input("book id: ")
    response = requests.put(
        f"http://127.0.0.1:8000/en/0/update/{book_id}", json=fields
        )
    return response.json()

def get_fields_inputs():
    fields = {
        "title": None,
        "originalTitle": None,
        "releaseDate": None,
        "description": None,
        "pages": None,
        "cover": None
        }
    for key, value in fields.items():
        value = None
        while value is None:
            value = input(key+": ")
            fields[key] = value
    return fields

fields = get_fields_inputs()
put_book_to_specific_id(fields)