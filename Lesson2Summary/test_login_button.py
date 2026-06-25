import pytest
from login_button import LoginButton


@pytest.fixture
def login_button():
    return LoginButton()


def test_get_label(login_button):
    assert login_button.get_label() == "Login"
    assert login_button.get_label() != "Login in"


def test_is_enabled(login_button):
    assert login_button.is_enabled() is True


def test_disable(login_button):
    login_button.disable()
    assert login_button.is_enabled() is False


def test_enable(login_button):
    login_button.disable()
    login_button.enable()
    assert login_button.is_enabled() is True


# def test_enable_disable(login_button):
#     login_button.disable()
#     assert login_button.is_enabled() is False
#     login_button.enable()
#     assert login_button.is_enabled() is True


@pytest.mark.parametrize("action, expected_result", [
    ("disable", False),
    ("enable", True)
])
def test_enable_disable(login_button, action, expected_result):
    login_button.disable()
    assert login_button.is_enabled() is False
    