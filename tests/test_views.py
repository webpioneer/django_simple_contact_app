from django.test import TestCase
from django.core.urlresolvers import reverse


class TestViews(TestCase):

    def setUp(self):
        self.contact_url = reverse('contact')

    def test_visit_contact_page(self):

        response = self.client.get(self.contact_url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'name')

    def test_post_email(self):
        data = {
            'name': 'John Doe',
            'email': 'john@email.com',
            'message': 'message body'
        }

        response = self.client.post(self.contact_url, data=data)

        self.assertEqual(response.status_code, 302)
