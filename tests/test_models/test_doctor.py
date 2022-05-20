#!/usr/bin/python3
"""
Contains the TestBaseUserDocs classes
"""

from datetime import datetime
import inspect
from models import doctor
from models.base_model import BaseModel
from models.permissions import Permissions
from models.base_user import BaseUser
import pep8
import storage
import unittest
BaseUser = base_user.BaseUser


class TestBaseUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseUser class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(BaseUser, inspect.isfunction)

    def test_pep8_conformance_base_user(self):
        """Test that models/base_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/base_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_user(self):
        """Test that tests/test_models/test_base_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_base_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_user_module_docstring(self):
        """Test for the base_user.py module docstring"""
        self.assertIsNot(base_user.__doc__, None,
                         "base_user.py needs a docstring")
        self.assertTrue(len(base_user.__doc__) >= 1,
                        "base_user.py needs a docstring")

    def test_base_user_class_docstring(self):
        """Test for the BaseUser class docstring"""
        self.assertIsNot(BaseUser.__doc__, None,
                         "BaseUser class needs a docstring")
        self.assertTrue(len(BaseUser.__doc__) >= 1,
                        "BaseUser class needs a docstring")

    def test_base_user_func_docstrings(self):
        """Test for the presence of docstrings in BaseUser methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestBaseUser(unittest.TestCase):