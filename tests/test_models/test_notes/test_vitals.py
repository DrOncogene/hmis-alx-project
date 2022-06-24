#!/usr/bin/python3
"""
Contains the TestVitalSignDocs classes
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models.patient import Patient
from models.notes import vitals
from tests.test_models.test_base_model import TestBaseModel

VitalSign = vitals.VitalSign


class TestVitalSignDocs(unittest.TestCase):
    """Tests to check the documentation and style of VitalSign class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.vitals_f = inspect.getmembers(VitalSign, inspect.isfunction)

    def test_pep8_conformance_vitals(self):
        """Test that models/notes/vitals.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/notes/vitals.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_vitals(self):
        """
        Test that tests/test_models/test_notes/test_vitals.py
        conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_models/test_notes/test_vitals.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_vitals_module_docstring(self):
        """Test for the vitals.py module docstring"""
        self.assertIsNot(vitals.__doc__, None,
                         "vitals.py needs a docstring")
        self.assertTrue(len(vitals.__doc__) >= 1,
                        "vitals.py needs a docstring")

    def test_vitals_class_docstring(self):
        """Test for the vitals class docstring"""
        self.assertIsNot(VitalSign.__doc__, None,
                         "VitalSign class needs a docstring")
        self.assertTrue(len(VitalSign.__doc__) >= 1,
                        "VitalSign class needs a docstring")

    def test_vitals_func_docstrings(self):
        """Test for the presence of docstrings in vitals methods"""
        for func in self.vitals_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestVitalSign(TestBaseModel):
    """Test the VitalSign class"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.patient = Patient()
        self.patient.save()
        self.tic = datetime.now()
        self.inst1 = VitalSign(pid=self.patient.pid)
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = VitalSign(pid=self.patient.pid)
        self.inst2.save()
        self.patient = storage.get(Patient, 'id', self.patient.id)
        self.inst1 = storage.get(VitalSign, 'id', self.inst1.id)
        self.vitals = self.inst1
        self.inst2 = storage.get(VitalSign, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.inst1.delete()
        self.inst2.delete()
        self.patient.delete()
        storage.save()

    def test_pid_attr(self):
        """Test that VitalSign has attr pid, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "pid"))
        self.assertEqual(self.vitals.pid, self.patient.pid)

    def test_consultation_id_attr(self):
        """
        Test that VitalSign has attr consultation_id,
        and it's an empty string
        """
        self.assertTrue(hasattr(self.vitals, "consultation_id"))
        self.assertEqual(self.vitals.consultation_id, None)

    def test_pr_attr(self):
        """Test that VitalSign has attr pr, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "pr"))
        self.assertEqual(self.vitals.pr, None)

    def test_rr_attr(self):
        """Test that VitalSign has attr rr, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "rr"))
        self.assertEqual(self.vitals.rr, None)

    def test_sbp_attr(self):
        """Test that VitalSign has attr sbp, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "sbp"))
        self.assertEqual(self.vitals.sbp, None)

    def test_dbp_attr(self):
        """Test that VitalSign has attr dbp, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "dbp"))
        self.assertEqual(self.vitals.sbp, None)

    def test_temp_attr(self):
        """Test that VitalSign has attr temp, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "temp"))
        self.assertEqual(self.vitals.temp, None)

    def test_spo2_attr(self):
        """Test that VitalSign has attr spo2, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "spo2"))
        self.assertEqual(self.vitals.spo2, None)

    def test_height_attr(self):
        """Test that VitalSign has attr height, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "height"))
        self.assertEqual(self.vitals.height, None)

    def test_weight_attr(self):
        """Test that VitalSign has attr weight, and it's an empty string"""
        self.assertTrue(hasattr(self.vitals, "weight"))
        self.assertEqual(self.vitals.weight, None)


if __name__ == '__main__':
    unittest.main()
