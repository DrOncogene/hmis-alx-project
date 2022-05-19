#!/usr/bin/python3
"""
Contains the TestBaseVitalsDocs classes
"""

from datetime import datetime
import inspect
import models
from models import vitals
from models.base_model import BaseModel
import pep8
import unittest
Vitals = vitals.Vitals


class TestVitalsDocs(unittest.TestCase):
    """Tests to check the documentation and style of Vitals class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.vitals_f = inspect.getmembers(Vitals, inspect.isfunction)

    def test_pep8_conformance_vitals(self):
        """Test that models/vitals.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/vitals.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_vitals(self):
        """Test that tests/test_models/test_vitals.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_vitals.py'])
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
        self.assertIsNot(Vitals.__doc__, None,
                         "Vitals class needs a docstring")
        self.assertTrue(len(Vitals.__doc__) >= 1,
                        "Vitals class needs a docstring")

    def test_vitals_func_docstrings(self):
        """Test for the presence of docstrings in vitals methods"""
        for func in self.vitals_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestVitals(unittest.TestCase):
    """Test the Vitals class"""
    def test_is_subclass(self):
        """Test that Vitals is a subclass of BaseModel"""
        vitals = Vitals()
        self.assertIsInstance(vitals, BaseModel)
        self.assertTrue(hasattr(vitals, "id"))
        self.assertTrue(hasattr(vitals, "created_at"))
        self.assertTrue(hasattr(vitals, "created_by"))
        self.assertTrue(hasattr(vitals, "updated_at"))
        self.assertTrue(hasattr(vitals, "updated_by"))

    def test_patient_id_attr(self):
        """Test that Vitals has attr patient_id, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "patient_id"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.patient_id, None)
        else:
            self.assertEqual(vitals.patient_id, "")

    def test_consult_id_attr(self):
        """Test that Vitals has attr consult_id, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "consult_id"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.consult_id, None)
        else:
            self.assertEqual(vitals.consult_id, "")

    def test_pr_attr(self):
        """Test that Vitals has attr pr, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "pr"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.pr, None)
        else:
            self.assertEqual(vitals.pr, "")

    def test_rr_attr(self):
        """Test that Vitals has attr rr, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "rr"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.rr, None)
        else:
            self.assertEqual(vitals.rr, "")

    def test_bp_attr(self):
        """Test that Vitals has attr bp, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "bp"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.bp, None)
        else:
            self.assertEqual(vitals.bp, "")

    def test_temp_attr(self):
        """Test that Vitals has attr temp, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "temp"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.temp, None)
        else:
            self.assertEqual(vitals.temp, "")

    def test_spo2_attr(self):
            """Test that Vitals has attr spo2, and it's an empty string"""
            vitals = Vitals()
            self.assertTrue(hasattr(vitals, "spo2"))
            if models.storage_t == 'db':
                self.assertEqual(vitals.spo2, None)
            else:
                self.assertEqual(vitals.spo2, "")

    def test_height_attr(self):
        """Test that Vitals has attr height, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "height"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.height, None)
        else:
            self.assertEqual(vitals.height, "")

    def test_weight_attr(self):
        """Test that Vitals has attr weight, and it's an empty string"""
        vitals = Vitals()
        self.assertTrue(hasattr(vitals, "weight"))
        if models.storage_t == 'db':
            self.assertEqual(vitals.weight, None)
        else:
            self.assertEqual(vitals.weight, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Vitals()
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
        u = Vitals()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Vitals")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        vitals = Vitals()
        string = "[Vitals] {}".format(vitals.__dict__)
        self.assertEqual(string, str(vitals))

if __name__ == '__main__':
    unittest.main()
