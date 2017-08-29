from django.test import TestCase

from django_contact.forms import ContactForm


class TestContactForm(TestCase):

    def test_contact_form(self):
        contact_form = ContactForm()

        # contact form has 3 fields
        self.assertEqual(len(contact_form.fields), 3)

    def test_contact_form_validation_for_blank_items(self):
        contact_form = ContactForm(data={})

        self.assertFalse(contact_form.is_valid())

        self.assertEqual(contact_form.errors['name'][0], u'This field is required.')

    def test_contact_form_valid(self):

        data = {
            'name': 'John',
            'email': 'john@email.com',
            'message': 'your website is amazing',
        }

        contact_form = ContactForm(data=data)

        self.assertTrue(contact_form.is_valid())

        self.assertEqual(contact_form.cleaned_data['email'], data['email'])
