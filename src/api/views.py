from flask_restful import reqparse, Resource
from flask import jsonify

from api.models import Book, User, Request
from api import db

parser = reqparse.RequestParser()

parser.add_argument('email')
parser.add_argument('title')


class RequestView(Resource):

    def get(self, book_id=None):
        if not book_id:
            return self._get_all_requests(book_id)

        return self._get_request(book_id)

    def post(self, book_id=None):
        args = parser.parse_args()
        book = self._get_book(args['title'])
        user = self._get_user(args['email'])

        if self._check_book_available(book, user):
            request = self._checkout_book(book, user)
            available = True
        else:
            available = False
            request = Request.query.filter_by(book_id=book.id).first()

        return jsonify({
            'id': book.id,
            'title': book.title,
            'available': available,
            'timestamp': request.timestamp
        })

    def delete(self, book_id):
        book = Book.query.filter_by(id=book_id).first()
        request = Request.query.filter_by(book_id=book.id).first()
        db.session.delete(request)
        db.session.commit()

    def _get_request(self, book_id):
        request = Request.query.filter_by(book_id=book_id).first()
        requests_result = {
            'book_id': request.book_id,
            'user_id': request.user_id,
            'timestamp': request.timestamp}
        return jsonify(requests_result)

    def _get_all_requests(self, book_id):
        requests = Request.query.all()
        requests_result = [{
            'book_id': request.book_id,
            'user_id': request.user_id,
            'timestamp': request.timestamp} for request in requests]
        return jsonify({'requests': requests_result})

    def _get_book(self, title):
        exists = db.session.query(Book.id).filter_by(
            title=title).scalar() is not None
        if not exists:
            # TO DO: add error handling
            raise ('This book is not in our library.')
        return Book.query.filter_by(title=title).first()

    def _get_user(self, email):
        exists = db.session.query(User.id).filter_by(
            email=email).scalar() is not None
        if not exists:
            raise ('This user does not exists.')  # TO DO: add error handling
        return User.query.filter_by(email=email).first()

    def _check_book_available(self, book, user):
        return not db.session.query(Request.id).filter_by(
            book_id=book.id,
            user_id=user.id).scalar()

    def _checkout_book(self, book, user):
        request = Request(
            user_id=user.id,
            book_id=book.id,
        )
        db.session.add(request)
        db.session.commit()
        return request
