#!/usr/bin/python3
"""
Contains the TestBaseDrugDocs classes
"""

from datetime import datetime
import inspect
import models
from models import drug
from models.base_model import BaseModel
import pep8
import unittest
Drug = drug.Drug


class TestDrugDocs(unittest.TestCase):
    """Tests to check the documentation and style of Drug class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.drug_f = inspect.getmembers(Drug, inspect.isfunction)

    def test_pep8_conformance_drug(self):
        """Test that models/drug.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/drug.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_drug(self):
        """Test that tests/test_models/test_drug.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_drug.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_drug_module_docstring(self):
        """Test for the drug.py module docstring"""
        self.assertIsNot(drug.__doc__, None,
                         "drug.py needs a docstring")
        self.assertTrue(len(drug.__doc__) >= 1,
                        "drug.py needs a docstring")

    def test_drug_class_docstring(self):
        """Test for the Drug class docstring"""
        self.assertIsNot(Drug.__doc__, None,
                         "Drug class needs a docstring")
        self.assertTrue(len(Drug.__doc__) >= 1,
                        "Drug class needs a docstring")

    def test_drug_func_docstrings(self):
        """Test for the presence of docstrings in Drug methods"""
        for func in self.drug_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestDrug(unittest.TestCase):
    """Test the Drug class"""
    def test_is_subclass(self):
        """Test that Drug is a subclass of BaseModel"""
        drug = Drug()
        self.assertIsInstance(drug, BaseModel)
        self.assertTrue(hasattr(drug, "id"))
        self.assertTrue(hasattr(drug, "created_at"))
        self.assertTrue(hasattr(drug, "created_by"))
        self.assertTrue(hasattr(drug, "updated_at"))
        self.assertTrue(hasattr(drug, "updated_by"))

    def test_name_attr(self):
        """Test that Drug has attr name, and it's an empty string"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "name"))
        if models.storage_t == 'db':
            self.assertEqual(drug.name, None)
        else:
            self.assertEqual(drug.name, "")

    def test_dose_attr(self):
        """Test that Drug has attr dose, and it's an empty string"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "dose"))
        if models.storage_t == 'db':
            self.assertEqual(drug.dose, None)
        else:
            self.assertEqual(drug.dose, "")

    def test_route_attr(self):
        """Test that Drug has attr route, and it's an empty string"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "route"))
        if models.storage_t == 'db':
            self.assertEqual(drug.route, None)
        else:
            self.assertEqual(drug.route, "")

    def test_brand_attr(self):
        """Test that Drug has attr brand, and it's an empty string"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "brand"))
        if models.storage_t == 'db':
            self.assertEqual(drug.brand, None)
        else:
            self.assertEqual(drug.brand, "")

    def test_formulation_attr(self):
        """Test that Drug has attr formulation, and it's an empty string"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "formulation"))
        if models.storage_t == 'db':
            self.assertEqual(drug.formulation, None)
        else:
            self.assertEqual(drug.formulation, "")

    def test_expiry_date_attr(self):
            """Test that Drug has attr expiry_date, and it's 0"""
            drug = Drug()
            self.assertTrue(hasattr(drug, "expiry_date"))
            if models.storage_t == 'db':
                self.assertEqual(drug.expiry_date, None)
            else:
                self.assertEqual(drug.expiry_date, 0)

    def test_stock_date_attr(self):
        """Test that Drug has attr stock_date, and it's 0"""
        drug = Drug()
        self.assertTrue(hasattr(drug, "stock_date"))
        if models.storage_t == 'db':
            self.assertEqual(drug.stock_date, None)
        else:
            self.assertEqual(drug.stock_date, 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Drug()
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
        u = Drug()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Drug")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        drug = Drug()
        string = "[Drug] {}".format(drug.__dict__)
        self.assertEqual(string, str(drug))


if __name__ == '__main__':
    unittest.main()
