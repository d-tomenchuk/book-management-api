
# Book Management API

An API for managing books and authors, built using FastAPI, SQLAlchemy, and Pydantic. This project provides functionality to create, read, update, and delete information about books and authors.

## Technologies

- **FastAPI** — for building the RESTful API.
- **SQLAlchemy** — for interacting with the database.
- **Pydantic** — for data validation and working with models.
- **SQLite** — for storing books and authors data.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/d-tomenchuk/book-management-api.git
cd book-management-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
source myenv/bin/activate  # For Linux or macOS
myenv\Scripts\activate  # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up the database

The project uses SQLite by default. No additional configuration is required. The SQLite database file will be created automatically when you run the application.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Docker Support

You can also run the application inside a Docker container.

### 1. Build the Docker image

```bash
docker build -t book-api .
```

### 2. Run the Docker container

```bash
docker run -d --name book-api -p 8000:8000 book-api
```

The application will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### Docker Compose (Optional)

The project includes a `docker-compose.yml` file for easier setup.

#### 1. Build and run the containers

```bash
docker-compose up --build
```

#### 2. Stop and remove the containers

```bash
docker-compose down
```

---

## Testing the API

You can test the API using:

### 1. **Pytest**

Run the tests using the following command:

```bash
pytest
```

### 2. **Postman**

#### Import API Endpoints

- Create a new collection in Postman.
- Add the following endpoints:

  **Authors**
  - `GET /authors` — Get all authors
  - `POST /authors` — Create a new author
  
    Sample Request:
    ```json
    {
      "name": "J.K. Rowling"
    }
    ```

  **Books**
  - `GET /books` — Get all books
  - `POST /books` — Create a new book
  
    Sample Request:
    ```json
    {
      "title": "Harry Potter and the Sorcerer's Stone",
      "description": "A young wizard's journey begins.",
      "author_id": 1
    }
    ```
  - `GET /books/{id}` — Get book details by ID
  - `PUT /books/{id}` — Update book information
  - `DELETE /books/{id}` — Delete a book

#### 3. Testing in Postman

- Use `POST /authors` to create an author.
- Use `POST /books` to create a book associated with the author.
- Test retrieval, updates, and deletions for the created data.

---


