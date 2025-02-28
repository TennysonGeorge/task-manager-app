from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Test Task', 'description': 'This is a test task.'})
    assert response.status_code == 201
    assert 'id' in response.get_json()

def test_get_task(client):
    response = client.get('/tasks/1')
    assert response.status_code == 200
    assert 'title' in response.get_json()

def test_update_task(client):
    response = client.put('/tasks/1', json={'title': 'Updated Task'})
    assert response.status_code == 200
    assert response.get_json()['title'] == 'Updated Task'

def test_delete_task(client):
    response = client.delete('/tasks/1')
    assert response.status_code == 204

def test_get_nonexistent_task(client):
    response = client.get('/tasks/999')
    assert response.status_code == 404