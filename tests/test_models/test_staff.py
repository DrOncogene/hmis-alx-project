#!/usr/bin/python3
"""
Contains the TestStaffDocs classes
"""

import inspect
import unittest
from datetime import datetime
import time

import pep8
from models import staff
from models.base_model import BaseModel
from models.base_user import BaseUser
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_base_model import TestBaseModel
from storage import storage

Staff = staff.Staff


class TestStaffDocs(unittest.TestCase):
    """Tests to check the documentation and style of Staff class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Staff, inspect.isfunction)

    def test_pep8_conformance_staff(self):
        """Test that models/staff.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/staff.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_staff(self):
        """Test that tests/test_models/test_staff.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_staff.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_staff_module_docstring(self):
        """Test for the staff.py module docstring"""
        self.assertIsNot(staff.__doc__, None,
                         "staff.py needs a docstring")
        self.assertTrue(len(staff.__doc__) >= 1,
                        "staff.py needs a docstring")

    def test_staff_class_docstring(self):
        """Test for the Staff class docstring"""
        self.assertIsNot(Staff.__doc__, None,
                         "Staff class needs a docstring")
        self.assertTrue(len(Staff.__doc__) >= 1,
                        "Staff class needs a docstring")

    def test_staff_func_docstrings(self):
        """Test for the presence of docstrings in Staff methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestStaff(unittest.TestCase):
    """Test the Staff class"""
    @classmethod
    def setUpClass(cls) -> None:
        if cls is not TestStaff:
            cls.is_base = False
        else:
            cls.is_base = True

    def setUp(self) -> None:
        if self.is_base:
            self.skipTest("Not testing baseuser")
        self.setUpBase()

    def tearDown(self) -> None:
        if self.is_base:
            self.skipTest("Not testing baseuser")
        self.tearDownBase()

    def test_is_subclass_baseuser(self):
        """Test that Staff is a subclass of BaseUser"""
        staff = self.staff
        self.assertIsInstance(staff, BaseUser)
        self.assertTrue(hasattr(staff, "first_name"))
        self.assertTrue(hasattr(staff, "last_name"))
        self.assertTrue(hasattr(staff, "gender"))
        self.assertTrue(hasattr(staff, "dob"))
        self.assertTrue(hasattr(staff, "email"))
        self.assertTrue(hasattr(staff, "marital_status"))
        self.assertTrue(hasattr(staff, "address"))
        self.assertTrue(hasattr(staff, "phone_number"))
        self.assertTrue(hasattr(staff, "next_of_kin"))
        self.assertTrue(hasattr(staff, "kin_address"))

    def test_staff_has_attr(self):
        """checks if staff object have correct attrs"""
        staff = self.staff
        self.assertTrue(hasattr(staff, "username"))
        self.assertTrue(hasattr(staff, "password"))
        self.assertTrue(hasattr(staff, "staff_id"))
        self.assertTrue(hasattr(staff, "staff_type"))
        self.assertTrue(hasattr(staff, "check_password"))
        self.assertTrue(hasattr(staff, "set_password"))

    def test_format_staff_id(self):
        """tests the format_staff_id method"""
        string = f"STF{self.staff.staff_id:04}"
        staff_id = self.staff.format_staff_id()
        self.assertEqual(string, staff_id)


if __name__ == '__main__':
    unittest.main()
