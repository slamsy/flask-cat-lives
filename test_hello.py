import pytest
import flask

from catlives import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_catty(client):
    """basic hello world"""

    rv = client.get('/')
    with client.session_transaction() as sess:
        sess['hangman'] = '{"alreadyGuessed": false, "answer": ["", "", "", "", "", ""], "guessedLetters": [], "hasLost": false, "hasWon": false, "numberOfGuesses": 6, "word": "macled", "wordLetters": ["m", "a", "c", "l", "e", "d"], "wordLettersRemaining": ["c", "m", "d", "a", "e", "l"]}'
    rv2 = client.get('/?guess=z')
    blankCount = rv2.data.count(b"blank\'")
    assert blankCount == 6
    assert b'5' in rv2.data
    rv3 = client.get('/?guess=m')
    assert b'5' in rv3.data #correct guess, no loss
    mCount = rv3.data.count(b">m<")
    assert mCount == 1
    rv4 = client.get('/?guess=n')
    rv5 = client.get('/?guess=o')
    rv6 = client.get('/?guess=p')
    rv7 = client.get('/?guess=q')
    rv8 = client.get('/?guess=r')
    assert b'0' in rv8.data
    assert b'CURSE' in rv8.data
