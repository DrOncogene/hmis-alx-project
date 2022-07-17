#!/usr/bin/python3
"""Test BaseModel for expected behavior and documentation"""
import inspect
import time
import unittest
from datetime import datetime
from unittest.mock import patch

import pep8 as pycodestyle
from models import base_model
from models.staff import Staff
from storage import storage

BaseModel = base_model.BaseModel
MODULE_DOC = base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(MODULE_DOC, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(MODULE_DOC) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    @classmethod
    def setUpClass(cls) -> None:
        if cls is not TestBaseModel:
            cls.is_base = False
        else:
            cls.is_base = True

    def setUp(self) -> None:
        if self.is_base:
            self.skipTest("Not testing basemodel")
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def test_instantiation(self):
        """Test that object is correctly created"""
        self.assertIsInstance(self.inst1, BaseModel)
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "created_by": type(None),
            "updated_at": datetime,
            "updated_by": type(None)
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, self.inst1.__dict__)
                self.assertIs(type(self.inst1.__dict__[attr]), typ)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        for inst in [self.inst1, self.inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(self.inst1.id, self.inst2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        inst_dict = self.inst1.to_dict()
        cls = type(self.inst1)
        expected_attrs = ["id",
                          "created_at",
                          "created_by",
                          "updated_at",
                          "updated_by"]
        for attr in expected_attrs:
            self.assertIn(attr, inst_dict.keys())

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        new_d = self.inst1.to_dict()
        self.assertEqual(type(new_d["created_at"]), datetime)
        self.assertEqual(type(new_d["updated_at"]), datetime)
        self.assertEqual(new_d["created_at"], self.inst1.created_at)
        self.assertEqual(new_d["updated_at"], self.inst1.updated_at)

    def test_str(self):
        """test that the str method has the correct output"""
        obj_dict = {}
        obj_dict.update(self.inst1.__dict__)
        if isinstance(self.inst1, Staff):
            obj_dict['staff_id'] = self.inst1.format_staff_id()
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        obj_dict.pop('_sa_instance_state', None)
        string = f"[{type(self.inst1).__name__}] {obj_dict}"
        self.assertEqual(string, str(self.inst1))

    def test_save(self):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        old_created_at = self.inst1.created_at
        old_updated_at = self.inst1.updated_at
        time.sleep(1)
        self.inst1.email = "email10"
        self.inst1.name = "name"
        self.inst1.pr = 135
        self.inst1.pc = "Fever x 3/7"
        self.inst1.note = "New note"
        self.inst1.save()
        new_created_at = self.inst1.created_at
        new_updated_at = self.inst1.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        with patch.object(storage, 'new') as mock_new:
            self.assertTrue(mock_new.assert_called)
        with patch.object(storage, 'save') as mock_save:
            self.assertTrue(mock_save.assert_called)

if __name__ == '__main__':
    unittest.main()
