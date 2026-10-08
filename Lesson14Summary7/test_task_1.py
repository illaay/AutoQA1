import requests
import pytest
from sandbox_api import SandboxApi
import json

BASE_URL = "https://api.qasandbox.org"


@pytest.fixture
def api():
    return SandboxApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    """Фикстура для получения токена перед тестами, требующими прав"""
    return api.get_auth_token("admin", "password")


# @pytest.fixture
# def sample_entity():
#     """Тестовые данные для создания брони"""
#     data = '{"name":"randomname","img":"https://images.unsplash.com/photo-1503152394-c571994fd383?w=400","desc":"random describe","category":"gods"}'
#     return json.loads(data)


def test_auth(api):
    assert api.get_auth_token("admin", "password")


def test_create_entity(api, auth_token):
    data = '{"name":"randomname1","img":"https://images.unsplash.com/photo-1503152394-c571994fd383?w=400","desc":"random describe","category":"gods"}'
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzg1NDg5NDc0LCJleHAiOjE3ODYwOTQyNzR9.4cPkXJ0hEpIC2ye689khHsLKFvP4ZsWCwmCOnlj8W48'
    resp = api.create_entity(json.loads(data), token)
    assert resp.status_code == 201
