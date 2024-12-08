# Book Management API

An API for managing books and authors, built using FastAPI, SQLAlchemy, and Pydantic. This project provides functionality to create, read, and update information about books and authors.

## Technologies

- **FastAPI** — for building the RESTful API.
- **SQLAlchemy** — for interacting with the database.
- **Pydantic** — for data validation and working with models.
- **PostgreSQL** — for storing books and authors data.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-repository/book-management-api.git
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

Create a database (e.g., PostgreSQL) and configure the database connection in the `.env` file.

### 5. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`.

## Docker Support

If you prefer to run the project inside a Docker container, you can use the provided `Dockerfile` and `docker-compose.yml` file.

### Running the application with Docker

1. Build the Docker image:

```bash
docker-compose build
```

2. Run the container:

```bash
docker-compose up
```

The application will be accessible at: `http://127.0.0.1:8000`.

Docker will automatically set up a PostgreSQL container and configure the database connection for you.

### Stopping the application

To stop the application and the containers:

```bash
docker-compose down
```

## API Endpoints

### /authors

- **GET /authors** — Get all authors
- **POST /authors** — Create a new author

### /books

- **GET /books** — Get all books
- **POST /books** — Create a new book
- **GET /books/{id}** — Get book details by ID
- **PUT /books/{id}** — Update book information
- **DELETE /books/{id}** — Delete a book

## Sample Requests

### Creating a new author

```bash
POST /authors
{
  "name": "J.K. Rowling"
}
```

### Creating a new book

```bash
POST /books
{
  "title": "Harry Potter and the Sorcerer's Stone",
  "description": "A young wizard's journey begins.",
  "author_id": 1
}
```

## Testing

You can run the tests using `pytest`:

```bash
pytest
```

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
