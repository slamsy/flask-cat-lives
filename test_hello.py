import pytest
import flask

from catlives import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_hello(client):
    """basic hello world"""

    rv = client.get('/')
    with client.session_transaction() as sess:
        sess['hangman'] = '{"alreadyGuessed": false, "answer": ["", "", "", "", "", ""], "guessedLetters": [], "hasLost": false, "hasWon": false, "numberOfGuesses": 6, "word": "macled", "wordLetters": ["m", "a", "c", "l", "e", "d"], "wordLettersRemaining": ["c", "m", "d", "a", "e", "l"]}'
    rv2 = client.get('/?guess=z')
    blankCount = rv2.data.count(b"blank\'")
    assert blankCount == 6
    assert b'5' in rv2.data
