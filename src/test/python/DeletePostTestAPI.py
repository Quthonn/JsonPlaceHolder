import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# Тест 3: Успешное удаление поста
def test_delete_post_success():
    post_id = 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code in [200, 204]
