from time import sleep

from Lesson6s2.constants.test_data import Credentials, FormData
from Lesson6s2.pages.contact_page import ContactPage


def test_fill_form(contact_page):
    contact_page.open()
    contact_page.fill_contact_form(name=FormData.NAME,
                                   email=FormData.EMAIL,
                                   phone=FormData.PHONE,
                                   subject=FormData.SUBJECT,
                                   message=FormData.MESSAGE)
    sleep(3)
    contact_page.submit_form()
    sleep(3)
    assert "Thanks for getting in touch" in contact_page.get_text(contact_page.SUCCESSFUL_TEXT)

def test_successful_login(auth_page):
    auth_page.open()