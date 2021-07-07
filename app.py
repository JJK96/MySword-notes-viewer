from flask import Flask, render_template
from dataclasses import dataclass
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect('versenotes.mybible')


@dataclass
class NoteBase:
    toverse: int
    fromverse: int
    data: str
    date: datetime
    title: str


class Note(NoteBase):
    def __init__(self, data=None, **kwargs):
        data = self.transform_data(data)
        super().__init__(data=data, **kwargs)

    def transform_data(self, data):
        # Delete titles
        soup = BeautifulSoup(data)
        for title in soup.select('h1'):
            title.extract()
        return soup


@app.route("/")
def books():
    return render_template('books.html')


@app.route("/<int:book>")
def book(book):
    paths = {}
    with get_db() as db:
        result = db.execute('select distinct chapter from commentary where book = ?', (book,))
        for i, row in enumerate(result):
            path = "/{}/{}".format(book, row[0])
            paths[path] = str(i+1)
    return render_template('book.html', paths=paths)


@app.route("/<int:book>/<int:chapter>")
def chapter(book, chapter):
    notes = []
    with get_db() as db:
        result = db.execute('select * from commentary where book = ? and chapter = ?', (book,chapter))
        for note in result:
            notes.append(Note(
                fromverse=note[3],
                toverse=note[4],
                data=note[5],
                date=note[6],
                title=note[8]
            ))
    chapter = f"Hoofdstuk {chapter}"
    return render_template('verse.html', notes=notes, chapter=chapter)


# @app.route("/<int:book>/<int:chapter>/<int:verse>")
# def verse(book, chapter, verse):
#     return 'Note text'
