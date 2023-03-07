#!/usr/bin/python3
"""
Contains the TestBasePrescriptionDocs classes
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models.patient import Patient
from models.notes.consult import Consultation
from models.notes import prescription
from models.drug import Drug
from tests.test_models.test_base_model import TestBaseModel

Prescription = prescription.Prescription
DrugPrescription = prescription.DrugPrescription


class TestPrescriptionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Prescription class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.prescription_f = inspect.getmembers(Prescription,
                                                inspect.isfunction)
        cls.DrugP_f = inspect.getmembers(DrugPrescription,
                                         inspect.isfunction)

    def test_pep8_conformance_prescription(self):
        """Test that models/notes/prescription.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/notes/prescription.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_prescription(self):
        """Test that tests/test_models/test_notes/test_prescription.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
                    ['tests/test_models/test_notes/test_prescription.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_prescription_module_docstring(self):
        """Test for the prescription.py module docstring"""
        self.assertIsNot(prescription.__doc__, None,
                         "prescription.py needs a docstring")
        self.assertTrue(len(prescription.__doc__) >= 1,
                        "prescription.py needs a docstring")

    def test_prescription_class_docstring(self):
        """Test for the Prescription class docstring"""
        self.assertIsNot(Prescription.__doc__, None,
                         "Prescription class needs a docstring")
        self.assertTrue(len(Prescription.__doc__) >= 1,
                        "Prescription class needs a docstring")

    def test_prescription_func_docstrings(self):
        """Test for the presence of docstrings in Prescription methods"""
        for func in self.prescription_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_drugprescription_class_docstring(self):
        """Test for the DrugPrescription class docstring"""
        self.assertIsNot(DrugPrescription.__doc__, None,
                         "DrugPrescription class needs a docstring")
        self.assertTrue(len(DrugPrescription.__doc__) >= 1,
                        "DrugPrescription class needs a docstring")

    def test_drugprescription_func_docstrings(self):
        """Test for the presence of docstrings in DrugPrescription methods"""
        for func in self.DrugP_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPrescription(TestBaseModel):
    """Test the prescription class"""
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
        self.inst2 = Prescription(
            pid=self.patient.pid,
            consultation_id=self.inst1.id
        )
        self.inst2.save()
        self.drug = Drug(name='Co-Amoxiclav', dose='625mg')
        self.drugpresc = DrugPrescription(
            drug_id=self.drug.id,
            prescription_id=self.inst2.id,
            dose='625mg',
            frequency='bd',
            route='oral',
            duration='1 week'
        )
        self.drug.save()
        self.drugpresc.save()
        self.patient = storage.get(Patient, 'id', self.patient.id)
        self.inst1 = storage.get(Consultation, 'id', self.inst1.id)
        self.inst2 = storage.get(Prescription, 'id', self.inst2.id)
        self.drugpresc = storage.get(DrugPrescription, 'id', self.drugpresc.id)
        self.consult = self.inst1
        self.prescription = self.inst2

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.patient.delete()
        storage.save()

    def test_pid_attr(self):
        """Test that prescription has attr pid"""
        self.assertTrue(hasattr(self.prescription, "pid"))
        self.assertEqual(self.prescription.pid, self.patient.pid)

    def test_consultation_id_attr(self):
        """Test that Prescription has attr consultation_id"""
        self.assertTrue(hasattr(self.prescription, "consultation_id"))
        self.assertEqual(self.prescription.consultation_id, self.consult.id)

    def test_drugs_attr(self):
        """Test that Prescription has attr drug_id,
        and it's a list of drug prescriptions"""
        self.assertTrue(hasattr(self.prescription, "drugs"))
        self.assertEqual(self.prescription.drugs, [self.drugpresc])

    def test_dispensed_by_attr(self):
        """Test that Prescription has attr dispensed_by,
        and it's None"""
        self.assertTrue(hasattr(self.prescription, "dispensed_by"))
        self.assertEqual(self.prescription.dispensed_by, None)

    def test_drug_id_attr(self):
        """Test that a DrugPrescription has attr drug_id"""
        self.assertTrue(hasattr(self.drugpresc, "drug_id"))
        self.assertEqual(self.drugpresc.drug_id, self.drug.id)

    def test_dose_attr(self):
        """Test that a DrugPrescription has attr dose"""
        self.assertTrue(hasattr(self.drugpresc, "dose"))
        self.assertEqual(self.drugpresc.dose, '625mg')

    def test_frequency_attr(self):
        """Test that a DrugPrescription has attr frequency"""
        self.assertTrue(hasattr(self.drugpresc, "frequency"))
        self.assertEqual(self.drugpresc.frequency, 'bd')

    def test_duration_attr(self):
        """Test that a DrugPrescription has attr duration"""
        self.assertTrue(hasattr(self.drugpresc, "duration"))
        self.assertEqual(self.drugpresc.duration, '1 week')

    def test_route_attr(self):
        """Test that a DrugPrescription has attr route"""
        self.assertTrue(hasattr(self.drugpresc, "route"))
        self.assertEqual(self.drugpresc.route, 'oral')


if __name__ == '__main__':
    unittest.main()
