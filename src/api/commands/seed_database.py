from flask_script import Command

from api import db
from api.models import Book, User


class SeedDB(Command):

    def run(self):
        self.add_user()
        self.add_books()
        db.session.commit()

    def add_user(self):
        email = 'elon@spacex.com'
        exists = db.session.query(User.id).filter_by(
            email=email).scalar() is not None
        if not exists:
            print('Adding the user {} to DB.'.format(email))
            user = User(email=email)
            db.session.add(user)

    def add_books(self):
        book_titles = [
            'The Death and Life of Great American Cities',
            'Salt, Fat, Acid, Heat',
            'The New Jim Crow'
        ]
        for title in book_titles:
            exists = db.session.query(Book.id).filter_by(
                title=title).scalar() is not None
            if not exists:
                print('Adding the book {} to DB.'.format(title))
                new_book = Book(title=title)
                db.session.add(new_book)
