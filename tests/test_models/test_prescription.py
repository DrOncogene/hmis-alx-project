#!/usr/bin/python3
"""
Contains the TestBasePrescriptionDocs classes
"""

from datetime import datetime
import inspect
import models
from models import prescription
from models.base_model import BaseModel
import pep8
import unittest
Prescription = prescription.Prescription


class TestPrescriptionDocs(unittest.TestCase):
    """Tests to check the documentation and style of Prescription class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.prescription_f = inspect.getmembers(Prescription,
                                                inspect.isfunction)

    def test_pep8_conformance_prescription(self):
        """Test that models/prescription.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/prescription.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_prescription(self):
        """Test that tests/test_models/test_prescription.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_prescription.py'])
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


class TestPrescription(unittest.TestCase):
    """Test the Prescription class"""
    def test_is_subclass(self):
        """Test that Prescription is a subclass of BaseModel"""
        prescription = Prescription()
        self.assertIsInstance(prescription, BaseModel)
        self.assertTrue(hasattr(prescription, "id"))
        self.assertTrue(hasattr(prescription, "created_at"))
        self.assertTrue(hasattr(prescription, "created_by"))
        self.assertTrue(hasattr(prescription, "updated_at"))
        self.assertTrue(hasattr(prescription, "updated_by"))

    def test_patient_id_attr(self):
        """Test that Prescription has attr patient_id,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "patient_id"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.patient_id, None)
        else:
            self.assertEqual(prescription.patient_id, "")

    def test_consult_id_attr(self):
        """Test that Prescription has attr consult_id,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "consult_id"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.consult_id, None)
        else:
            self.assertEqual(prescription.consult_id, "")

    def test_drug_id_attr(self):
        """Test that Prescription has attr drug_id,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "drug_id"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.drug_id, None)
        else:
            self.assertEqual(prescription.drug_id, "")

    def test_dose_attr(self):
        """Test that Prescription has attr dose,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "dose"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.dose, None)
        else:
            self.assertEqual(prescription.dose, 0)

    def test_unit_attr(self):
        """Test that Prescription has attr unit,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "unit"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.unit, None)
        else:
            self.assertEqual(prescription.unit, "")

    def test_frequency_attr(self):
            """Test that Prescription has attr frequency,
            and it's an empty string"""
            prescription = Prescription()
            self.assertTrue(hasattr(prescription, "frequency"))
            if models.storage_t == 'db':
                self.assertEqual(prescription.frequency, None)
            else:
                self.assertEqual(prescription.frequency, "")

    def test_duration_attr(self):
        """Test that Prescription has attr duration,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "duration"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.duration, None)
        else:
            self.assertEqual(prescription.duration, "")

    def test_period_attr(self):
        """Test that Prescription has attr period,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "period"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.period, None)
        else:
            self.assertEqual(prescription.period, "")

    def test_route_attr(self):
        """Test that Prescription has attr route,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "route"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.route, None)
        else:
            self.assertEqual(prescription.route, "")

    def test_dispensed_by_attr(self):
        """Test that Prescription has attr dispensed_by,
        and it's an empty string"""
        prescription = Prescription()
        self.assertTrue(hasattr(prescription, "dispensed_by"))
        if models.storage_t == 'db':
            self.assertEqual(prescription.dispensed_by, None)
        else:
            self.assertEqual(prescription.dispensed_by, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Prescription()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Prescription()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Prescription")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        prescription = Prescription()
        string = "[Prescription] {}".format(prescription.__dict__)
        self.assertEqual(string, str(prescription))

if __name__ == '__main__':
    unittest.main()
