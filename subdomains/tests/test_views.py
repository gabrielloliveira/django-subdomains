from http import HTTPStatus

from django.test import TestCase, override_settings


class TestViews(TestCase):
    fixtures = ["subdomains.json"]

    def test_index_view_returns_status_200(self):
        """Index view should return status 200, with content_type JSON"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {"subdomain": None})

    @override_settings(ALLOWED_HOSTS=[".testserver"])
    def test_index_view_returns_subdomain_api(self):
        """Index view should return status 200, with content_type JSON"""
        response = self.client.get("http://api.testserver/", HTTP_HOST="api.testserver")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json(), {"subdomain": "api"})
