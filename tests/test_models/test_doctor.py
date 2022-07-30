#!/usr/bin/python3
"""
unittest module to test doctor class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import doctor
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_staff import TestStaff

Doctor = doctor.Doctor


class TestDoctorDocs(unittest.TestCase):
    """Tests to check the documentation and style of Doctor class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Doctor, inspect.isfunction)

    def test_pep8_conformance_doctor(self):
        """Test that models/doctor.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/doctor.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_doctor(self):
        """Test that tests/test_models/test_doctor.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_doctor.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doctor_module_docstring(self):
        """Test for the doctor.py module docstring"""
        self.assertIsNot(doctor.__doc__, None,
                         "doctor.py needs a docstring")
        self.assertTrue(len(doctor.__doc__) >= 1,
                        "doctor.py needs a docstring")

    def test_doctor_class_docstring(self):
        """Test for the BaseUser class docstring"""
        self.assertIsNot(Doctor.__doc__, None,
                         "Doctor class needs a docstring")
        self.assertTrue(len(Doctor.__doc__) >= 1,
                        "Doctor class needs a docstring")

    def test_doctor_func_docstrings(self):
        """Test for the presence of docstrings in Doctor methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDoctor(TestBaseModel, TestBaseUser, TestStaff):
    """tests the Doctor"""
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
        self.inst1 = Doctor(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Doctor(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.staff = self.user = storage.get(Staff, 'id', self.user.id)
        self.doctor = self.inst1 = storage.get(Doctor, 'id', self.inst1.id)
        self.inst2 = storage.get(Doctor, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check doctor obj for attr"""
        doctor = self.doctor
        self.assertIsInstance(doctor, Staff)
        self.assertTrue(hasattr(doctor, 'job_title'))
        self.assertEqual(doctor.job_title, 'Doctor')
        self.assertTrue(hasattr(doctor, 'roles'))


if __name__ == '__main__':
    unittest.main()
