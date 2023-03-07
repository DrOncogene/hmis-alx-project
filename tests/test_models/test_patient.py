#!/usr/bin/python3
"""
unittest module to test doctor class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import patient
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import BaseUser, TestBaseUser
from tests.test_models.test_staff import TestStaff

Patient = patient.Patient


class TestPatientDocs(unittest.TestCase):
    """Tests to check the documentation and style of Patient class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(patient, inspect.isfunction)

    def test_pep8_conformance_patient(self):
        """Test that models/patient.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/patient.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_patient(self):
        """Test that tests/test_models/test_patient.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_patient.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_patient_module_docstring(self):
        """Test for the patient.py module docstring"""
        self.assertIsNot(patient.__doc__, None,
                         "patient.py needs a docstring")
        self.assertTrue(len(patient.__doc__) >= 1,
                        "patient.py needs a docstring")

    def test_patient_class_docstring(self):
        """Test for the Patient class docstring"""
        self.assertIsNot(Patient.__doc__, None,
                         "Patient class needs a docstring")
        self.assertTrue(len(Patient.__doc__) >= 1,
                        "Patient class needs a docstring")

    def test_patient_func_docstrings(self):
        """Test for the presence of docstrings in Patient methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPatient(TestBaseModel, TestBaseUser):
    """tests the Patient model"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.user = Patient(
            email='email',
            username='username',
            password='password'
        )
        self.user.save()
        self.tic = datetime.now()
        self.inst1 = Patient(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Patient(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.patient = self.user = storage.get(Patient, 'id', self.user.id)
        self.inst1 = storage.get(Patient, 'id', self.inst1.id)
        self.inst2 = storage.get(Patient, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check patient obj for attr"""
        patient = self.patient
        self.assertIsInstance(patient, BaseUser)
        self.assertTrue(hasattr(patient, 'pid'))
        self.assertTrue(hasattr(patient, 'consultations'))
        self.assertTrue(hasattr(patient, 'prescriptions'))
        self.assertTrue(hasattr(patient, 'vitals'))
        self.assertTrue(hasattr(patient, 'nursenotes'))


if __name__ == '__main__':
    unittest.main()
