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