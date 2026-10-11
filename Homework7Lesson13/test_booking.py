import pytest
from .booking_api import BookerApi


BASE_URL = "https://restful-booker.herokuapp.com"

# пришлось отказаться от scope='class', сохранив атомарность тестов,
# так как requests с ним стала ругаться на ssl-сертфикаты
@pytest.fixture
def api():
    return BookerApi(BASE_URL)


@pytest.fixture
def auth_token(api):
    return api.get_auth_token("admin", "password123")


@pytest.fixture
def sample_booking():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }


class TestBookingSystem:

    def test_create_booking(self, api, sample_booking):
        created_data = api.create_booking(sample_booking)
        assert "bookingid" in created_data
        assert created_data["booking"]["firstname"] == sample_booking["firstname"]

    def test_partial_update_booking(self, api, auth_token, sample_booking):
        created = api.create_booking(sample_booking)
        booking_id = created["bookingid"]
        patch_payload = {
            "firstname": "Alexander",
            "totalprice": 500
        }
        resp = api.partial_update_booking(booking_id, patch_payload, auth_token)
        assert resp.status_code == 200
        patched_data = resp.json()
        assert patched_data["firstname"] == "Alexander"
        assert patched_data["totalprice"] == 500

    def test_negative_update_with_invalid_token(self, api, sample_booking):
        created = api.create_booking(sample_booking)
        booking_id = created["bookingid"]
        patch_payload = {"firstname": "Hacker"}
        resp = api.partial_update_booking(booking_id, patch_payload, "bad_token_123")
        assert resp.status_code == 403

    def test_delete_booking(self, api, auth_token, sample_booking):
        created = api.create_booking(sample_booking)
        booking_id = created["bookingid"]
        delete_resp = api.delete_booking(booking_id, auth_token)
        assert delete_resp.status_code == 201
        get_resp = api.get_booking(booking_id)
        assert get_resp.status_code == 404
