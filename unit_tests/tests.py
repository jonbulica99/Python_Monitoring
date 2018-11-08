import unittest
import unit_tests
import random
import string
from client import Client


class BaseTest(unittest.TestCase):
    def __init__(self, name):
        super().__init__()
        self.name = name

class ModuleTest(BaseTest):
    def __init__(self):
        super().__init__(__class__.__name__)
        self.client = Client()

    def test_supported_checks(self):
        self.all_checks = self.client.get_supported_checks()
        self.assertTrue(self.all_checks is not None and len(self.all_checks) > 0)

    def test_exceptions_reflection(self):
        self.assertTrue(self.client.check_by_name(None) is None)
        with self.assertRaises(ImportError):
            random_name = "".join( [random.choice(string.ascii_letters) for i in xrange(15)] )
            self.client.check_by_name(random_name)

    def test_checks_default(self):
        self.assertTrue(self.client.check_by_name("cpu") is not None)

    def test_system_status(self):
        self.assertTrue(self.client.system_status() is not None)

if __name__ == '__main__':
    unittest.main()