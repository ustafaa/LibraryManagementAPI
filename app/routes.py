# app/routes.py
import json
import os
from flask import Blueprint, jsonify, request
from .schema import BookSchema


api = Blueprint('api', __name__)
BOOKS_FILE = 'data/books.json'

def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, 'r') as f:
            data = json.load(f)
            return data.get('books', [])
    return []

def save_books(books):
    os.makedirs(os.path.dirname(BOOKS_FILE), exist_ok=True)
    with open(BOOKS_FILE, 'w') as f:
        json.dump({'books': books}, f, indent=2)

@api.route('/books', methods=['POST'])
def add_book():
    schema = BookSchema()
    try:
        book_data = schema.load(request.json)
        books = load_books()
        
        if any(book.get('isbn') == book_data.get('isbn') for book in books):
            return {'error': 'ISBN already exists'}, 400
            
        books.append(book_data)
        save_books(books)
        return jsonify(book_data), 201
    except Exception as e:
        return {'error': str(e)}, 400

@api.route('/books', methods=['GET'])
def list_books():
    books = load_books()
    author = request.args.get('author')
    year = request.args.get('published_year')
    genre = request.args.get('genre')
    
    if author:
        books = [b for b in books if b.get('author', '').lower() == author.lower()]
    if year:
        books = [b for b in books if str(b.get('published_year')) == year]
    if genre:
        books = [b for b in books if b.get('genre', '').lower() == genre.lower()]
        
    return jsonify(books)

@api.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    books = load_books()
    books = [b for b in books if b['isbn'] != isbn]
    save_books(books)
    return '', 204

@api.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    schema = BookSchema(partial=True)
    update_data = schema.load(request.json)
    
    books = load_books()
    for book in books:
        if book['isbn'] == isbn:
            book.update(update_data)
            save_books(books)
            return jsonify(book)
            
    return {'error': 'Book not found'}, 404

@api.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    books = load_books()
    for book in books:
        if book['isbn'] == isbn:
            return jsonify(book)
    return {'error': 'Book not found'}, 404
