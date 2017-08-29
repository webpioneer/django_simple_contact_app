# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from selenium import webdriver


class TestContactPage(TestCase):
    """Test functional Contact Page"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_send_email(self):
        # user visits contact page
        self.browser.get("http://127.0.0.1:8001/contact-us/")

        contact_form = self.browser.find_element_by_name("contact-form")

        # fill out form

        name_input = contact_form.find_element_by_name('name')
        name_input.send_keys('John Doe')

        email_input = contact_form.find_element_by_name('email')
        email_input.send_keys('john@email.com')

        message_text_area = contact_form.find_element_by_name('message')
        message_text_area.send_keys('Your website is amazing')

        contact_form.submit()
