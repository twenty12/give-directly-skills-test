from flask_script import Command
from api import db
from api.models import Book, User


class SeedDB(Command):

    def run(self):
        self.add_user()
        self.add_books()
        db.session.commit()

    def add_user(self):
        user = User(email='elon@spacex.com')
        db.session.add(user)

    def add_books(self):
        book_titles = [
            'The Death and Life of Great American Cities',
            'Salt, Fat, Acid, Heat',
            'The New Jim Crow'
        ]
        for title in book_titles:
            new_book = Book(title=title)
            db.session.add(new_book)
