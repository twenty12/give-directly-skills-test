import requests

BASE_URL = 'http://0.0.0.0:5000/'


class TestIntegration:
    def add_request(self):
        payload = {
            'email': 'elon@spacex.com',
            'title': 'The New Jim Crow'
        }
        self.book_id = requests.post(
            BASE_URL + '/request',
            data=payload).json()['id']

    def remove_request(self):
        url = '{}/request/{}'.format(
            BASE_URL,
            self.book_id
        )
        requests.delete(url)

    def test_get_all_requests(self):
        self.add_request()
        response = requests.get(BASE_URL + '/request')
        assert len(response.json()['requests']) == 1
        self.remove_request()

    def test_get_specific_request(self):
        self.add_request()
        url = '{}/request/{}'.format(BASE_URL, self.book_id)
        response = requests.get(url)
        assert response.json()['book_id'] == self.book_id
        self.remove_request()

    def test_remove_existing_request(self):
        self.add_request()
        url = '{}/request/{}'.format(
            BASE_URL,
            self.book_id
        )
        response = requests.delete(url)
        assert response.ok

    def test_request_book_with_valid_email(self):
        payload = {
            'email': 'elon@spacex.com',
            'title': 'The New Jim Crow'
        }
        response = requests.post(BASE_URL + '/request', data=payload)
        data = response.json()
        assert data['available']

        # Cleanup
        url = '{}/request/{}'.format(
            BASE_URL,
            data['id']
        )
        response = requests.delete(url)

    def test_request_non_existent_book_with_valid_email(self):
        payload = {
            'email': 'elon@spacex.com',
            'title': 'Becoming'
        }
        response = requests.post(BASE_URL + '/request', data=payload)
        assert not response.ok

    def test_request_unavaible_book_with_valid_email(self):
        payload = {
            'email': 'elon@spacex.com',
            'title': 'The New Jim Crow'
        }
        requests.post(BASE_URL + '/request', data=payload)
        response = requests.post(BASE_URL + '/request', data=payload)
        data = response.json()
        assert not data['available']

        url = '{}/request/{}'.format(
            BASE_URL,
            data['id']
        )
        response = requests.delete(url)
