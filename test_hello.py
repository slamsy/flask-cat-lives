import pytest

from hello import hello

@pytest.fixture
def client():
    hello.app.config['TESTING'] = True
    client = hello.app.test_client()

    yield client

def test_hello(client):
    """basic hello world"""

    rv = client.get('/hello')
    assert b'Hello' in rv.data
