#!/usr/bin/python3
"""
Contains the TestStaffDocs classes
"""

from datetime import datetime
import inspect
from models import staff
from models.base_model import BaseModel
from models.permissions import Permissions
from models.base_user import BaseUser
import pep8
import storage
import unittest
Staff = staff.Staff


class TestStaffDocs(unittest.TestCase):
    """Tests to check the documentation and style of Staff class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Staff, inspect.isfunction)

    def test_pep8_conformance_staff(self):
        """Test that models/staff.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/staff.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_staff(self):
        """Test that tests/test_models/test_staff.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_staff.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_staff_module_docstring(self):
        """Test for the staff.py module docstring"""
        self.assertIsNot(staff.__doc__, None,
                         "staff.py needs a docstring")
        self.assertTrue(len(staff.__doc__) >= 1,
                        "staff.py needs a docstring")

    def test_staff_class_docstring(self):
        """Test for the Staff class docstring"""
        self.assertIsNot(Staff.__doc__, None,
                         "Staff class needs a docstring")
        self.assertTrue(len(Staff.__doc__) >= 1,
                        "Staff class needs a docstring")

    def test_staff_func_docstrings(self):
        """Test for the presence of docstrings in Staff methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestStaff(unittest.TestCase):
    """Test the Staff class"""
    def test_is_subclass(self):
        """Test that Staff is a subclass of BaseModel"""
        staff = Staff()
        self.assertIsInstance(staff, BaseModel)
        self.assertTrue(hasattr(staff, "id"))
        self.assertTrue(hasattr(staff, "created_at"))
        self.assertTrue(hasattr(staff, "created_by"))
        self.assertTrue(hasattr(staff, "updated_at"))
        self.assertTrue(hasattr(staff, "updated_by"))

    def test_is_subclass(self):
        """Test that Staff is a subclass of BaseUser"""
        staff = Staff()
        self.assertIsInstance(staff, BaseUser)
        self.assertTrue(hasattr(staff, "first_name"))
        self.assertTrue(hasattr(staff, "last_name"))
        self.assertTrue(hasattr(staff, "gender"))
        self.assertTrue(hasattr(staff, "dob"))
        self.assertTrue(hasattr(staff, "marital_status"))
        self.assertTrue(hasattr(staff, "address"))
        self.assertTrue(hasattr(staff, "telephone_number"))
        self.assertTrue(hasattr(staff, "kinfirst_name"))
        self.assertTrue(hasattr(staff, "kinlast_name"))
        self.assertTrue(hasattr(staff, "kincontact_address"))

    def test_is_subclass(self):
        """Test that Staff is a subclass of Permissions"""
        staff = Staff()
        self.assertIsInstance(staff, Permissions)
        self.assertTrue(hasattr(staff, "items"))
        self.assertTrue(hasattr(staff, "create"))
        self.assertTrue(hasattr(staff, "delete"))
        self.assertTrue(hasattr(staff, "view"))
        self.assertTrue(hasattr(staff, "edit"))

    def test_job_title_attr(self):
        """Test that BaseUser has attr job_title, and it's an empty string"""
        staff = Staff()
        self.assertTrue(hasattr(staff, "job_title"))
        if storage.storage_t == 'db':
            self.assertEqual(staff.job_title, None)
        else:
            self.assertEqual(staff.job_title, "")

    """def test_set_staff_id(self):
        """Test that staff id is correctly created"""
        staff = Staff()
        self.assertIs(type(staff), Staff)
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "created_by": str,
            "updated_at": datetime,
            "updated_by": str
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, inst.__dict__)
                self.assertIs(type(inst.__dict__[attr]), typ)
    
    @mock.patch('storage.storage')
    def test_set_staff_id(self, mock_storage):
        """Test that set_staff_id method `"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        self.assertTrue(mock_storage.new.assert_called)
        self.assertTrue(mock_storage.save.assert_called)"""

if __name__ == '__main__':
    unittest.main()
