from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    title: str
    author: str
    published_year: int
    isbn: str
    genre: Optional[str] = None
    