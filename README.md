## API Practice Project
In this project, I practiced getting data via API and creating my own API using Requests and FastAPI.

For ingesting data, I used PotterAPI (https://github.com/fedeperin/potterapi). PotterAPI is a Harry Potter API developed with Express.js and available in multiple languages.
This API stores information and images of books, characters and spells. 

Contents:
- Extracting data via the API with inputs for language and data( i.g., language: en, artifact: books)
- Naming the data with the input and store them in parquet format ( i.g., books-en.parquet)
- Handling unexpected inputs
- Cleaning the parquet files by converting the column names

For creating an API, I used the data from the PotterAPI again as example data.

Contents:
- Set the content of data and data structure
- Writing the response to different requests (get, post, and put)
