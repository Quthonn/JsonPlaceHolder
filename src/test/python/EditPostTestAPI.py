import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

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
