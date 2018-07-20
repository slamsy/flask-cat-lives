import pytest

from hello import hello

@pytest.fixture
def client():
    flaskr.app.config['TESTING'] = true
    client = flaskr.app.test_client()

    yield client
