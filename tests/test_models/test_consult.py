#!/usr/bin/python3
"""
Contains the TestBaseConsultDocs classes
"""

from datetime import datetime
import inspect
import models
from models import consult
from models.base_model import BaseModel
import pep8
import unittest
Consult = consult.Consult


class TestConsultDocs(unittest.TestCase):
    """Tests to check the documentation and style of Consult class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.consult_f = inspect.getmembers(Consult, inspect.isfunction)

    def test_pep8_conformance_consult(self):
        """Test that models/consult.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/consult.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_consult(self):
        """Test that tests/test_models/test_consult.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_consult.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_consult_module_docstring(self):
        """Test for the Consult.py module docstring"""
        self.assertIsNot(consult.__doc__, None,
                         "consult.py needs a docstring")
        self.assertTrue(len(consult.__doc__) >= 1,
                        "consult.py needs a docstring")

    def test_consult_class_docstring(self):
        """Test for the Consult class docstring"""
        self.assertIsNot(Consult.__doc__, None,
                         "Consult class needs a docstring")
        self.assertTrue(len(Consult.__doc__) >= 1,
                        "Consult class needs a docstring")

    def test_consult_func_docstrings(self):
        """Test for the presence of docstrings in Consult methods"""
        for func in self.consult_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestConsult(unittest.TestCase):
    """Test the Consult class"""
    def test_is_subclass(self):
        """Test that Consult is a subclass of BaseModel"""
        consult = Consult()
        self.assertIsInstance(consult, BaseModel)
        self.assertTrue(hasattr(consult, "id"))
        self.assertTrue(hasattr(consult, "created_at"))
        self.assertTrue(hasattr(consult, "created_by"))
        self.assertTrue(hasattr(consult, "updated_at"))
        self.assertTrue(hasattr(consult, "updated_by"))

    def test_patient_id_attr(self):
        """Test that Consult has attr patient_id, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "patient_id"))
        if models.storage_t == 'db':
            self.assertEqual(consult.patient_id, None)
        else:
            self.assertEqual(consult.patient_id, "")

    def test_prescription_id_attr(self):
        """Test that Consult has attr prescription_id, and it's a list"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "prescription_id"))
        if models.storage_t == 'db':
            self.assertEqual(consult.prescription_id, None)
        else:
            self.assertEqual(consult.prescription_id, [])

    def test_vitals_id_attr(self):
        """Test that Consult has attr vitals_id, and it's a list"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "vitals_id"))
        if models.storage_t == 'db':
            self.assertEqual(consult.vitals_id, None)
        else:
            self.assertEqual(consult.vitals_id, [])

    def test_pc_attr(self):
        """Test that Consult has attr pc, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "pc"))
        if models.storage_t == 'db':
            self.assertEqual(consult.pc, None)
        else:
            self.assertEqual(consult.pc, "")

    def test_hpc_attr(self):
        """Test that Consult has attr hpc, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "hpc"))
        if models.storage_t == 'db':
            self.assertEqual(consult.hpc, None)
        else:
            self.assertEqual(consult.hpc, "")

    def test_pohx_attr(self):
        """Test that Consult has attr pohx, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "pohx"))
        if models.storage_t == 'db':
            self.assertEqual(consult.pohx, None)
        else:
            self.assertEqual(consult.pohx, "")

    def test_pghx_attr(self):
            """Test that Consult has attr pghx, and it's an empty string"""
            consult = Consult()
            self.assertTrue(hasattr(consult, "pghx"))
            if models.storage_t == 'db':
                self.assertEqual(consult.pghx, None)
            else:
                self.assertEqual(consult.pghx, "")

    def test_pmhx_attr(self):
        """Test that Consult has attr pmhx, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "pmhx"))
        if models.storage_t == 'db':
            self.assertEqual(consult.pmhx, None)
        else:
            self.assertEqual(consult.pmhx, "")

    def test_prov_diag_attr(self):
        """Test that Consult has attr prov_diag, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "prov_diag"))
        if models.storage_t == 'db':
            self.assertEqual(consult.prov_diag, None)
        else:
            self.assertEqual(consult.prov_diag, "")

    def test_plan_attr(self):
        """Test that Consult has attr plan, and it's an empty string"""
        consult = Consult()
        self.assertTrue(hasattr(consult, "plan"))
        if models.storage_t == 'db':
            self.assertEqual(consult.plan, None)
        else:
            self.assertEqual(consult.plan, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Consult()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Consult()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Consult")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        consult = Consult()
        string = "[Consult] {}".format(consult.__dict__)
        self.assertEqual(string, str(consult))

if __name__ == '__main__':
    unittest.main()
