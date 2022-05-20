#!/usr/bin/python3
"""
Contains the TestBaseConsultationDocs classes
"""

from datetime import datetime
import inspect
from models.base_model import BaseModel
from models.notes import consult
import pep8
import storage
import unittest
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
        """Test that tests/test_models/test_models_notes/test_consult.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_models_notes/test_consult.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_consult_module_docstring(self):
        """Test for the consult.py module docstring"""
        self.assertIsNot(consult.__doc__, None,
                         "consult.py needs a docstring")
        self.assertTrue(len(consult.__doc__) >= 1,
                        "consult.py needs a docstring")

    def test_consult_class_docstring(self):
        """Test for the Consultation class docstring"""
        self.assertIsNot(Consultation.__doc__, None,
                         "Consultation class needs a docstring")
        self.assertTrue(len(Consultation.__doc__) >= 1,
                        "Consultation class needs a docstring")

    def test_consult_func_docstrings(self):
        """Test for the presence of docstrings in Consultation methods"""
        for func in self.consult_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestConsultation(unittest.TestCase):
    """Test the Consultation class"""
    def test_is_subclass(self):
        """Test that Consultation is a subclass of BaseModel"""
        consult = Consultation()
        self.assertIsInstance(consult, BaseModel)
        self.assertTrue(hasattr(consult, "id"))
        self.assertTrue(hasattr(consult, "created_at"))
        self.assertTrue(hasattr(consult, "created_by"))
        self.assertTrue(hasattr(consult, "updated_at"))
        self.assertTrue(hasattr(consult, "updated_by"))

    def test_pid_attr(self):
        """Test that Consultation has attr pid, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "pid"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.pid, None)
        else:
            self.assertEqual(consult.pid, "")

    def test_prescription_ids_attr(self):
        """Test that Consultation has attr prescription_ids, and it's a list"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "prescription_ids"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.prescription_ids, None)
        else:
            self.assertEqual(consult.prescription_ids, [])

    def test_vitals_id_attr(self):
        """Test that Consultation has attr vitals_id, and it's a list"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "vitals_id"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.vitals_id, None)
        else:
            self.assertEqual(consult.vitals_id, [])

    def test_pc_attr(self):
        """Test that Consultation has attr pc, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "pc"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.pc, None)
        else:
            self.assertEqual(consult.pc, "")

    def test_hpc_attr(self):
        """Test that Consultation has attr hpc, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "hpc"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.hpc, None)
        else:
            self.assertEqual(consult.hpc, "")

    def test_pohx_attr(self):
        """Test that Consultation has attr pohx, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "pohx"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.pohx, None)
        else:
            self.assertEqual(consult.pohx, "")

    def test_pghx_attr(self):
            """Test that Consultation has attr pghx, and it's an empty string"""
            consult = Consultation()
            self.assertTrue(hasattr(consult, "pghx"))
            if storage.storage_t == 'db':
                self.assertEqual(consult.pghx, None)
            else:
                self.assertEqual(consult.pghx, "")

    def test_pmhx_attr(self):
        """Test that Consultation has attr pmhx, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "pmhx"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.pmhx, None)
        else:
            self.assertEqual(consult.pmhx, "")

    def test_prov_diag_attr(self):
        """Test that Consultation has attr prov_diag, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "prov_diag"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.prov_diag, None)
        else:
            self.assertEqual(consult.prov_diag, "")

    def test_plan_attr(self):
        """Test that Consultation has attr plan, and it's an empty string"""
        consult = Consultation()
        self.assertTrue(hasattr(consult, "plan"))
        if storage.storage_t == 'db':
            self.assertEqual(consult.plan, None)
        else:
            self.assertEqual(consult.plan, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Consultation()
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
        u = Consultation()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Consultation")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        consult = Consultation()
        string = "[Consultation] {}".format(consult.__dict__)
        self.assertEqual(string, str(consult))

if __name__ == '__main__':
    unittest.main()
