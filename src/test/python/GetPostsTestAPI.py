import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Тест 1: Успешное создание поста
def test_create_post_success():
    payload = {
        "title": "Fast Food",
        "body": "Shef, give me burger, please",
        "userId": 1324
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

# Тест 2: Успешное изменение поста
def test_update_post_success():
    post_id = 1
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/{post_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert data["id"] == post_id

# Тест 3: Успешное удаление поста
def test_delete_post_success():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code in [200, 204]
