from django.test import TestCase
from django.urls import reverse


class SnacksTest(TestCase):
    def test_home_page_status_code(self):
        url = reverse('snack_list')
        print(f"The url is {url}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
