from unittest import mock

from django.test import TestCase, override_settings
from django.test.client import RequestFactory

from subdomains.middleware import SubdomainMiddleware
from subdomains.models import Subdomain
from subdomains.views import index


class TestSubdomainMiddleware(TestCase):
    fixtures = ["subdomains.json"]

    def setUp(self):
        self.factory = RequestFactory()

    def test_request_without_middleware_has_not_subdomain_attr(self):
        """if the request does not go through the middleware, then it does not have the subdomain attribute"""
        request = self.factory.get("/")
        with self.assertRaises(AttributeError):
            index(request)

    def test_middleware_insert_subdomain_attr_in_request(self):
        """SubdomainMiddleware should insert subdomain attribute in request object"""
        get_response = mock.MagicMock()
        request = self.factory.get("/")

        middleware = SubdomainMiddleware(get_response)
        _ = middleware(request)

        self.assertTrue(hasattr(request, "subdomain"))

    @override_settings(ALLOWED_HOSTS=[".testserver"])
    def test_middleware_insert_subdomain_instance_in_request(self):
        """SubdomainMiddleware should insert SubdomainModel instance in request object"""
        get_response = mock.MagicMock()
        request = self.factory.get("/", HTTP_HOST="app.testserver")

        middleware = SubdomainMiddleware(get_response)
        response = middleware(request)

        self.assertTrue(isinstance(request.subdomain, Subdomain))
        self.assertEqual(response.status_code, response.status_code)
