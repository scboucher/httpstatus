import pytest
import http_status
@pytest.fixture
def client():
    http_status.app.config['TESTING'] = True
    client = http_status.app.test_client()
    with http_status.app.app_context():
        pass
    yield client

 

def test_get_slash(client):
    """Test Get / is not allowed."""

    rv = client.get('/')
    assert 405 == rv.status_code

def test_post_slash(client):
    """Test Post / ."""
    rv = client.post('/', data=dict(text=400) )
    assert 200 == rv.status_code
    assert b'Bad Request' in rv.data


def test_post_slash_invalid_code(client):
    """Test Post / . with invalid status code"""
    rv = client.post('/', data=dict(text=527) )
    assert 200 == rv.status_code
    assert b'Invalid Status Code' in rv.data

def test_post_slash_empty(client):
    """Test Post / . with Empty data should return the help"""
    rv = client.post('/', data=dict(text="") )
    assert 200 == rv.status_code
    assert b':catshake:' in rv.data