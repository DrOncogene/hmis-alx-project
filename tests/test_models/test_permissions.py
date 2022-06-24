#!/usr/bin/python3
"""
Contains the TestPermissionDocs classes
"""

import inspect
import unittest

import pep8
from models import permissions

Permission = permissions.Permission


class TestPermissionsDocs(unittest.TestCase):
    """Tests to check the documentation and style of Permission class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Permission, inspect.isfunction)

    def test_pep8_conformance_permissions(self):
        """Test that models/permissions.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/permissions.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_permissions(self):
        """Test that tests/test_models/test_permissions.py conforms to PEP8."""
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(['tests/test_models/test_permissions.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_permissions_module_docstring(self):
        """Test for the permissions.py module docstring"""
        self.assertIsNot(permissions.__doc__, None,
                         "permissions.py needs a docstring")
        self.assertTrue(len(permissions.__doc__) >= 1,
                        "permissions.py needs a docstring")

    def test_permissions_class_docstring(self):
        """Test for the Permission class docstring"""
        self.assertIsNot(Permission.__doc__, None,
                         "Permission class needs a docstring")
        self.assertTrue(len(Permission.__doc__) >= 1,
                        "Permission class needs a docstring")

    def test_permissions_func_docstrings(self):
        """Test for the presence of docstrings in Permission methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPermissions(unittest.TestCase):
    """Test the Permission class"""


if __name__ == '__main__':
    unittest.main()
