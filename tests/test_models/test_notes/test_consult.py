#!/usr/bin/python3
"""
Contains the TestConsultationDocs classes
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models.patient import Patient
from models.notes import consult
from models.notes.vitals import VitalSign
from models.notes.prescription import Prescription
from tests.test_models.test_base_model import TestBaseModel

Consultation = consult.Consultation


class TestConsultationDocs(unittest.TestCase):
    """Tests to check the documentation and style of Consultation class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.consult_f = inspect.getmembers(Consultation, inspect.isfunction)

    def test_pep8_conformance_consult(self):
        """Test that models/notes/consult.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/notes/consult.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_consult(self):
        """
        Test that tests/test_models/test_notes/test_consult.py
        conforms to PEP8.
        """
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_models/test_notes/test_consult.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_consult_module_docstring(self):
        """Test for the consult.py module docstring"""
        self.assertIsNot(consult.__doc__, None,
                         "consult.py needs a docstring")
        self.assertTrue(len(consult.__doc__) >= 1,
                        "consult.py needs a docstring")

    def test_consult_class_docstring(self):
        """Test for the consult class docstring"""
        self.assertIsNot(Consultation.__doc__, None,
                         "Consultation class needs a docstring")
        self.assertTrue(len(Consultation.__doc__) >= 1,
                        "Consultation class needs a docstring")

    def test_consult_func_docstrings(self):
        """Test for the presence of docstrings in consult methods"""
        for func in self.consult_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestConsultation(TestBaseModel):
    """Test the Consultation class"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.patient = Patient()
        self.patient.save()
        self.patient = storage.get(Patient, 'id', self.patient.id)
        self.tic = datetime.now()
        self.inst1 = Consultation(
            pid=self.patient.pid,
            prov_diag='Malaria'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Consultation(
            pid=self.patient.pid,
            prov_diag='URTI'
        )
        self.inst2.save()
        self.vitals = VitalSign(
            pid=self.patient.pid,
            consultation_id=self.inst1.id
        )
        self.vitals.save()
        self.prescription = Prescription(
            pid=self.patient.pid,
            consultation_id=self.inst1.id
        )
        self.prescription.save()
        self.patient = storage.get(Patient, 'id', self.patient.id)
        self.inst1 = storage.get(Consultation, 'id', self.inst1.id)
        self.consult = self.inst1
        self.inst2 = storage.get(Consultation, 'id', self.inst2.id)
        self.vitals = storage.get(VitalSign, 'id', self.vitals.id)
        self.prescription = storage.get(Prescription, 'id',
                                        self.prescription.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.inst1.delete()
        self.inst2.delete()
        self.patient.delete()
        self.vitals.delete()
        storage.save()

    def test_pid_attr(self):
        """Test that Consultation has attr pid, and it's an None"""
        self.assertTrue(hasattr(self.consult, "pid"))
        self.assertEqual(self.consult.pid, self.patient.pid)

    def test_prescriptions_attr(self):
        """Test that Consultation has attr prescription_ids, and it's a list"""
        self.assertTrue(hasattr(self.consult, "prescriptions"))
        self.assertEqual(self.consult.prescriptions, [self.prescription])

    def test_vitals_attr(self):
        """Test that Consultation has attr vitals_id, and it's a list"""
        self.assertTrue(hasattr(self.consult, "vitals"))
        self.assertEqual(self.consult.vitals, [self.vitals])

    def test_pc_attr(self):
        """Test that Consultation has attr pc, and it's an None"""
        self.assertTrue(hasattr(self.consult, "pc"))
        self.assertEqual(self.consult.pc, None)

    def test_hpc_attr(self):
        """Test that Consultation has attr hpc, and it's an None"""
        self.assertTrue(hasattr(self.consult, "hpc"))
        self.assertEqual(self.consult.hpc, None)

    def test_pohx_attr(self):
        """Test that Consultation has attr pohx, and it's an None"""
        self.assertTrue(hasattr(self.consult, "pohx"))
        self.assertEqual(self.consult.pohx, None)

    def test_pghx_attr(self):
        """Test that Consultation has attr pghx, and it's an None"""
        self.assertTrue(hasattr(self.consult, "pghx"))
        self.assertEqual(self.consult.pghx, None)

    def test_pmhx_attr(self):
        """Test that Consultation has attr pmhx, and it's an None"""
        self.assertTrue(hasattr(self.consult, "pmhx"))
        self.assertEqual(self.consult.pmhx, None)

    def test_prov_diag_attr(self):
        """Test that Consultation has attr prov_diag,
        and it's an None"""
        self.assertTrue(hasattr(self.consult, "prov_diag"))
        self.assertEqual(self.consult.prov_diag, "Malaria")

    def test_plan_attr(self):
        """Test that Consultation has attr plan, and it's an None"""
        self.assertTrue(hasattr(self.consult, "plan"))
        self.assertEqual(self.consult.plan, None)


if __name__ == '__main__':
    unittest.main()
