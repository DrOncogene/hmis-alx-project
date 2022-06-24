#!/usr/bin/python3
"""
Contains the TestBaseUserDocs classes
"""

from datetime import datetime
import inspect
import unittest

import pep8
from models import base_user
from models.base_model import BaseModel
from models.staff import Staff

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
    """Test the BaseUser class"""

    @classmethod
    def setUpClass(cls) -> None:
        if cls is not TestBaseUser:
            cls.is_base = False
        else:
            cls.is_base = True

    def setUp(self) -> None:
        if self.is_base:
            self.skipTest("Not testing baseuser")
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def test_is_subclass(self):
        """Test that BaseUser is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "created_by"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertTrue(hasattr(self.user, "updated_by"))

    def test_first_name_attr(self):
        """Test that BaseUser has attr first_name, and it's an empty string"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, None)

    def test_last_name_attr(self):
        """Test that BaseUser has attr last_name, and it's an empty string"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, None)

    def test_gender_attr(self):
        """Test that BaseUser has attr gender, and it's an empty string"""
        self.assertTrue(hasattr(self.user, "gender"))
        self.assertEqual(self.user.gender, None)

    def test_email_attr(self):
        """Test that BaseUser has attr email, and it's an empty string"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "email")

    def test_dob_attr(self):
        """Test that BaseUser has attr dob, and it's empty"""
        self.assertTrue(hasattr(self.user, "dob"))
        self.assertEqual(self.user.dob, None)

    def test_marital_status_attr(self):
        """Test that BaseUser has attr marital_status,
        and it's an empty string"""
        self.assertTrue(hasattr(self.user, "marital_status"))
        self.assertEqual(self.user.marital_status, None)

    def test_address_attr(self):
        """Test that BaseUser has attr address, and it's an empty string"""
        self.assertTrue(hasattr(self.user, "address"))
        self.assertEqual(self.user.address, None)

    def test_phone_number_attr(self):
        """Test that BaseUser has attr telephone_number,
        and it's an empty string"""
        self.assertTrue(hasattr(self.user, "phone_number"))
        self.assertEqual(self.user.phone_number, None)

    def test_next_of_kin_attr(self):
        """Test that BaseUser has attr next_of_kin,
        and it's an empty string"""
        self.assertTrue(hasattr(self.user, "next_of_kin"))
        self.assertEqual(self.user.next_of_kin, None)

    def test_kin_address_attr(self):
        """Test that BaseUser has attr kin_address,
        and it's an empty string"""
        self.assertTrue(hasattr(self.user, "kin_address"))
        self.assertEqual(self.user.kin_address, None)


if __name__ == '__main__':
    unittest.main()
