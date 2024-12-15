
### Library Management API

A RESTful API for managing a library's book collection, built with Flask and Docker.

## Features
- Add/Update/Delete books
- Search by author, year, or genre
- Swagger documentation
- Docker containerization
- AWS EC2 deployment

## Live Demo
The API is deployed and accessible at:
http://ec2-52-59-226-250.eu-central-1.compute.amazonaws.com

## Local Development

### Prerequisites
- Docker
- Git
- Python 3.9+

### Quick Start
```bash
# Clone repository
git clone https://github.com/yourusername/LibraryManagementAPI.git
cd LibraryManagementAPI

# Build Docker image
docker build -t library-api .

# Run container
docker run -d -p 5000:5000 library-api
```

## API Documentation
- Local: http://localhost:4000/api-docs
- Production: http://ec2-52-59-226-250.eu-central-1.compute.amazonaws.com/api-docs/

## Development

### Branch Protection
The `main` branch is protected with:
- Required PR reviews
- Pre-merge checks must pass:
    - Unit tests
    - Linting (min score: 9.0)
    - API endpoint verification

### Running Tests Locally
```bash
# Run tests
python -m pytest -v

# Run linting
pylint app/*.py tests/*.py --fail-under=9.0
```

## API Endpoints

### Books
- `POST /api/books` - Add new book
- `GET /api/books` - List all books
- `GET /api/books?author=&year=&genre=` - Search books
- `PUT /api/books/{isbn}` - Update book
- `DELETE /api/books/{isbn}` - Delete book

## Docker Commands
```bash
# Build image
docker build -t library-api .

# Run container
docker run -d -p 4000:4000 library-api

# View logs
docker logs library-api

# Stop container
docker stop library-api
```

## Environment Variables
- `PORT` - API port (default: 5000)
- `DEBUG` - Enable debug mode (default: False)

## Deployment
The API is deployed on AWS EC2. You can:
- Access Swagger docs: http://ec2-52-59-226-250.eu-central-1.compute.amazonaws.com
- Test endpoints directly through Swagger UI
- Use standard HTTP clients like curl or Postman
```
