import sys

from django.conf import settings
from django.test.utils import get_runner

from boot_django import boot_django

if __name__ == "__main__":
    boot_django()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["subdomains.tests"])
    sys.exit(bool(failures))
