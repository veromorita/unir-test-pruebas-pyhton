import http.client
import os
import unittest
import urllib.request
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

    def test_api_subtract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "2")

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/2/3"
        response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "6")

    def test_api_divide_by_zero(self):
        url = f"{BASE_URL}/calc/divide/1/0"
        try:
            response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertIn("Division by zero", e.read().decode())
    
    def test_api_log10_negative(self):
        url = f"{BASE_URL}/calc/log10/-1"
        try:
            response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertIn("Logarithm undefined for non-positive values", e.read().decode())

    def test_api_sqrt(self):
        url = f"{BASE_URL}/calc/sqrt/9"
        response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(response.read().decode(), "3.0")

    def test_api_log10_zero(self):
        url = f"{BASE_URL}/calc/log10/0"
        try:
            response = urllib.request.urlopen(url, timeout=DEFAULT_TIMEOUT)
        except urllib.error.HTTPError as e:
            self.assertEqual(e.code, http.client.BAD_REQUEST)
            self.assertIn("Logarithm undefined for non-positive values", e.read().decode())

        
if __name__ == "__main__":  # pragma: no cover
    unittest.main()