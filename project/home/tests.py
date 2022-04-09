from django.test import TestCase

# Create your tests here.
class HomeTestCase(TestCase):

    def test_home_response(self):
        response = self.client.get("/")
        self.assertEqual(response.json(), {"msg": "Home is where your heart is."})
