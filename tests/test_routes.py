# tests/test_routes.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_book(client):
    book = {
        "title": "Test Book",
        "author": "Test Author", 
        "published_year": 2024,
        "isbn": "1234567890",
        "genre": "Fiction"
    }
    response = client.post('/api/books', json=book)
    assert response.status_code == 201

def test_get_all_books(client):
    response = client.get('/api/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_search_books(client):
    response = client.get('/api/books?author=Test Author')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_delete_book(client):
    response = client.delete('/api/books/1234567890')
    assert response.status_code == 204

def test_update_book(client):
    update_data = {
        "title": "Updated Book Title",
        "genre": "Non-Fiction" 
    }
    response = client.put('/api/books/1234567890', json=update_data)
    assert response.status_code == 200 or response.status_code == 404

def test_invalid_isbn(client):
    response = client.get('/api/books/invalid_isbn')
    assert response.status_code == 404

def test_add_book_missing_required_fields(client):
    book = {
        "title": "Test Book"
    }
    response = client.post('/api/books', json=book)
    assert response.status_code == 400
    