from flask import Flask, render_template, request
from dataclasses import dataclass
from datetime import datetime
from bs4 import BeautifulSoup
from books import get_book, books as book_list
import sqlite3
import os

app = Flask(__name__)


def get_db():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'versenotes.mybible')
    return sqlite3.connect(filename)


@dataclass
class NoteBase:
    toverse: int
    fromverse: int
    data: str
    date: datetime
    title: str
    book: str = None
    chapter: int = None


class Note(NoteBase):
    def __init__(self, data=None, book=None, **kwargs):
        data = self.transform_data(data)
        super().__init__(data=data, book=get_book(book), **kwargs)

    def transform_data(self, data):
        # Delete titles
        soup = BeautifulSoup(data)
        for title in soup.select('h1'):
            title.extract()
            # Extract only the first title
            break
        return soup

    @classmethod
    def from_db(self, note):
        return Note(
            fromverse=note[3],
            toverse=note[4],
            data=note[5],
            date=note[6],
            title=note[8],
            book=note[1],
            chapter=note[2],
        )


@app.route("/")
def books():
    book_dict = {i+1: book for i, book in enumerate(book_list)}
    return render_template('books.html', books=book_dict)


@app.route("/search")
def search():
    query = request.args.get("q")
    query = "%" + query + "%"
    notes = []
    with get_db() as db:
        result = db.execute('select * from commentary where title like ? or data like ?', (query, query))
        for note in result:
            notes.append(Note.from_db(note))
    return render_template('search.html', notes=notes, title="Resultaten")


@app.route("/<int:book>/")
def book(book):
    paths = {}
    with get_db() as db:
        result = db.execute('select distinct chapter from commentary where book = ?', (book,))
        for row in result:
            path = str(row[0])
            paths[path] = str(row[0])
    return render_template('book.html', paths=paths)


@app.route("/<int:book>/<int:chapter>")
def chapter(book, chapter):
    notes = []
    with get_db() as db:
        result = db.execute('select * from commentary where book = ? and chapter = ?', (book, chapter))
        for note in result:
            notes.append(Note.from_db(note))
    title = f"Hoofdstuk {chapter}"
    return render_template('chapter.html', notes=notes, title=title, chapter=chapter)
