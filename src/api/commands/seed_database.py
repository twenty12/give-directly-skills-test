from flask_script import Command
from api import db
from api.models import Book


class SeedDB(Command):

    def run(self):
        book_titles = [
            'The Death and Life of Great American Cities',
            'Salt, Fat, Acid, Heat',
            'The New Jim Crow'
        ]
        for title in book_titles:
            new_book = Book(title=title)
            db.session.add(new_book)
            db.session.commit()
