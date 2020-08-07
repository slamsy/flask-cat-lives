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
        sess['catlives'] = '{"CorrectorIncorrect": true, "alreadyGuessed": false, "answer": ["", "", "", "", "", ""], "guessedLetters": "", "guessedLetters": [], "hasLost": false, "hasWon": false, "numberOfGuesses": 9, "word": "macled", "wordLetters": ["m", "a", "c", "l", "e", "d"], "wordLettersRemaining": ["m", "a", "c", "l", "e", "d"], "wrongLetters": []}'
    mCount1 = rv.data.count(b"m")
    rv2 = client.get('/?guess=z')
    blankCount = rv2.data.count(b"\'blank")
    assert blankCount == 6
    assert b'dying' in rv2.data
    rv3 = client.get('/?guess=m')
    assert b'dying' not in rv3.data
    assert b'dead' in rv3.data #correct guess, no loss
    assert b'newBlankGuess' in rv3.data
    mCount2 = rv3.data.count(b"m")
    assert mCount2 == mCount1 + 1
    rv4 = client.get('/?guess=n')
    rv5 = client.get('/?guess=o')
    rv6 = client.get('/?guess=p')
    rv7 = client.get('/?guess=q')
    rv8 = client.get('/?guess=r')
    rv8 = client.get('/?guess=s')
    rv8 = client.get('/?guess=t')
    rv8 = client.get('/?guess=u')
    assert b'0' in rv8.data
    assert b'CURSE' in rv8.data
