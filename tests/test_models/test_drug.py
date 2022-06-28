#!/usr/bin/python3
"""
Contains the TestBaseDrugDocs classes
"""

from datetime import datetime
import inspect
import unittest

import pep8
from storage import storage
from models import drug
from models.base_model import BaseModel
from tests.test_models.test_base_model import TestBaseModel

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


class TestDrug(TestBaseModel):
    """Test the Drug class"""

    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.drug = Drug()
        self.drug.save()
        self.tic = datetime.now()
        self.inst1 = Drug(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = Drug(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.drug = storage.get(Drug, 'id', self.drug.id)
        self.inst1 = storage.get(Drug, 'id', self.inst1.id)
        self.inst2 = storage.get(Drug, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.drug.delete()
        self.inst1.delete()
        self.inst2.delete()
        storage.save()

    def test_is_subclass(self):
        """Test that Drug is a subclass of BaseModel"""
        self.assertIsInstance(self.drug, BaseModel)
        self.assertTrue(hasattr(self.drug, "id"))
        self.assertTrue(hasattr(self.drug, "created_at"))
        self.assertTrue(hasattr(self.drug, "created_by"))
        self.assertTrue(hasattr(self.drug, "updated_at"))
        self.assertTrue(hasattr(self.drug, "updated_by"))

    def test_name_attr(self):
        """Test that Drug has attr name, and it's an empty string"""
        self.assertTrue(hasattr(self.drug, "name"))
        self.assertEqual(self.drug.name, None)

    def test_dose_attr(self):
        """Test that Drug has attr dose, and it's an empty string"""
        self.assertTrue(hasattr(self.drug, "dose"))
        self.assertEqual(self.drug.dose, None)

    def test_route_attr(self):
        """Test that Drug has attr route, and it's an empty string"""
        self.assertTrue(hasattr(self.drug, "route"))
        self.assertEqual(self.drug.route, None)

    def test_brand_attr(self):
        """Test that Drug has attr brand, and it's an empty string"""
        self.assertTrue(hasattr(self.drug, "brand"))
        self.assertEqual(self.drug.brand, None)

    def test_formulation_attr(self):
        """Test that Drug has attr formulation, and it's an empty string"""
        self.assertTrue(hasattr(self.drug, "formulation"))
        self.assertEqual(self.drug.formulation, None)

    def test_expiry_date_attr(self):
            """Test that Drug has attr expiry_date, and it's 0"""
            self.assertTrue(hasattr(self.drug, "expiry_date"))
            self.assertEqual(self.drug.expiry_date, None)

    def test_stock_date_attr(self):
        """Test that Drug has attr stock_date, and it's 0"""
        self.assertTrue(hasattr(self.drug, "stock_date"))
        self.assertEqual(self.drug.stock_date, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        new_d = self.drug.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in self.drug.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)


if __name__ == '__main__':
    unittest.main()
