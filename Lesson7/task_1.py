import requests
import pytest
import json

base_url = "https://reqres.in/api"


def test_api():

    response = requests.get(base_url)

    assert response.status_code == 200
    res = response.json()
    length_features = len(res["features"])
    print(res['name'])
    print(res['endpoints']['health'])
    print(length_features)
    assert res['name'] == 'ReqRes API'
    assert res['endpoints']['health'] == '/health'
    assert length_features == 4