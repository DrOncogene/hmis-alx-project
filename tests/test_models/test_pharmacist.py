#!/usr/bin/python3
"""
unittest module to test pharmacist class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import pharmacist
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_staff import TestStaff

Pharmacist = pharmacist.Pharmacist


class TestpharmacistDocs(unittest.TestCase):
    """Tests to check the documentation and style of Pharmacist class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(pharmacist, inspect.isfunction)

    def test_pep8_conformance_pharmacist(self):
        """Test that models/pharmacist.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/pharmacist.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_pharmacist(self):
        """Test that tests/test_models/test_pharmacist.py conforms to PEP8."""
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(['tests/test_models/test_pharmacist.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pharmacist_module_docstring(self):
        """Test for the pharmacist.py module docstring"""
        self.assertIsNot(pharmacist.__doc__, None,
                         "pharmacist.py needs a docstring")
        self.assertTrue(len(pharmacist.__doc__) >= 1,
                        "pharmacist.py needs a docstring")

    def test_pharmacist_class_docstring(self):
        """Test for the Pharmacist class docstring"""
        self.assertIsNot(Pharmacist.__doc__, None,
                         "Pharmacist class needs a docstring")
        self.assertTrue(len(Pharmacist.__doc__) >= 1,
                        "Pharmacist class needs a docstring")

    def test_pharmacist_func_docstrings(self):
        """Test for the presence of docstrings in Pharmacist methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPharmacist(TestBaseModel, TestBaseUser, TestStaff):
    """tests the pharmacist"""
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
        self.inst1 = Pharmacist(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Pharmacist(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.staff = self.user = storage.get(Staff, 'id', self.user.id)
        self.pharmacist = self.inst1 =\
            storage.get(Pharmacist, 'id', self.inst1.id)
        self.inst2 = storage.get(Pharmacist, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check pharmacist obj for attr"""
        pharmacist = self.pharmacist
        self.assertIsInstance(pharmacist, Staff)
        self.assertTrue(hasattr(pharmacist, 'job_title'))
        self.assertEqual(pharmacist.job_title, 'Pharmacist')
        self.assertTrue(hasattr(pharmacist, 'roles'))


if __name__ == '__main__':
    unittest.main()
