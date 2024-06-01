import unittest
from scanner import sql_injection, xss, directory_traversal

class TestScanner(unittest.TestCase):

    def test_sql_injection(self):
        result = sql_injection.scan("http://example.com/?id=")
        self.assertIn(result, ["Vulnerable", "Not Vulnerable"])

    def test_xss(self):
        result = xss.scan("http://example.com/?q=")
        self.assertIn(result, ["Vulnerable", "Not Vulnerable"])

    def test_directory_traversal(self):
        result = directory_traversal.scan("http://example.com/")
        self.assertIn(result, ["Vulnerable", "Not Vulnerable"])

if __name__ == '__main__':
    unittest.main()
