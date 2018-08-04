import pytest
import flask

from hello import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_hello(client):
    """basic hello world"""

    rv = client.get('/')
    with client.session_transaction() as sess:
        sess['hangman'] = '{"CorrectorIncorrect": false, "answer": ["", "", "", ""], "guessedLetters": ["z", "z"], "numberOfGuesses": 6, "numberofGuesses": 5, "word": "test", "wordLetters": ["t", "e", "s", "t"], "wordLettersRemaining": ["t", "e", "s"]}'
    rv2 = client.get('/?guess=z')
    blankCount = rv2.data.count(b"blank\'")
    assert blankCount == 4
    assert b'5' in rv.data
