import pytest

from hello import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_hello(client):
    """basic hello world"""

    rv = client.get('/hello')
    assert b'hello' in rv.data
