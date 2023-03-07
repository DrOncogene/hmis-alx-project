#!/usr/bin/python3
"""
unittest module to test nurse class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import nurse
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_staff import TestStaff

Nurse = nurse.Nurse


class TestNurseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Nurse class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Nurse, inspect.isfunction)

    def test_pep8_conformance_nurse(self):
        """Test that models/nurse.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/nurse.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_nurse(self):
        """Test that tests/test_models/test_nurse.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_nurse.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_nurse_module_docstring(self):
        """Test for the nurse.py module docstring"""
        self.assertIsNot(nurse.__doc__, None,
                         "nurse.py needs a docstring")
        self.assertTrue(len(nurse.__doc__) >= 1,
                        "nurse.py needs a docstring")

    def test_nurse_class_docstring(self):
        """Test for the Nurse class docstring"""
        self.assertIsNot(Nurse.__doc__, None,
                         "Nurse class needs a docstring")
        self.assertTrue(len(Nurse.__doc__) >= 1,
                        "Nurse class needs a docstring")

    def test_nurse_func_docstrings(self):
        """Test for the presence of docstrings in Nurse methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestNurse(TestBaseModel, TestBaseUser, TestStaff):
    """tests the Nurse"""
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
        self.inst1 = Nurse(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Nurse(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.staff = self.user = storage.get(Staff, 'id', self.user.id)
        self.nurse = self.inst1 = storage.get(Nurse, 'id', self.inst1.id)
        self.inst2 = storage.get(Nurse, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check nurse obj for attr"""
        nurse = self.nurse
        self.assertIsInstance(nurse, Staff)
        self.assertTrue(hasattr(nurse, 'job_title'))
        self.assertEqual(nurse.job_title, 'Nurse')
        self.assertTrue(hasattr(nurse, 'role'))


if __name__ == '__main__':
    unittest.main()
