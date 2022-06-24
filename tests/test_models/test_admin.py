#!/usr/bin/python3
"""
unittest module to test admin class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import admin
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_staff import TestStaff

Admin = admin.Admin


class TestadminDocs(unittest.TestCase):
    """Tests to check the documentation and style of Admin class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(admin, inspect.isfunction)

    def test_pep8_conformance_admin(self):
        """Test that models/admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_admin(self):
        """Test that tests/test_models/test_admin.py conforms to PEP8."""
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(['tests/test_models/test_admin.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_admin_module_docstring(self):
        """Test for the admin.py module docstring"""
        self.assertIsNot(admin.__doc__, None,
                         "admin.py needs a docstring")
        self.assertTrue(len(admin.__doc__) >= 1,
                        "admin.py needs a docstring")

    def test_admin_class_docstring(self):
        """Test for the Admin class docstring"""
        self.assertIsNot(Admin.__doc__, None,
                         "Admin class needs a docstring")
        self.assertTrue(len(Admin.__doc__) >= 1,
                        "Admin class needs a docstring")

    def test_admin_func_docstrings(self):
        """Test for the presence of docstrings in Admin methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAdmin(TestBaseModel, TestBaseUser, TestStaff):
    """tests the admin"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.user = Staff(
            email='email',
            username='username',
            password='password'
        )
        self.user.save()
        self.tic = datetime.now()
        self.inst1 = Admin(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Admin(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.staff = self.user = storage.get(Staff, 'id', self.user.id)
        self.admin = self.inst1 =\
            storage.get(Admin, 'id', self.inst1.id)
        self.inst2 = storage.get(Admin, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        self.staff.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check admin obj for attr"""
        admin = self.admin
        self.assertIsInstance(admin, Staff)
        self.assertTrue(hasattr(admin, 'job_title'))
        self.assertEqual(admin.job_title, 'Admin')
        self.assertTrue(hasattr(admin, 'permissions'))


if __name__ == '__main__':
    unittest.main()
