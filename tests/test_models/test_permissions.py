#!/usr/bin/python3
"""
Contains the TestPermissionsDocs classes
"""

from datetime import datetime
import inspect
from models import permissions
from models.base_model import BaseModel
import pep8
import storage
import unittest
Permissions = permissions.Permissions


class TestPermissionsDocs(unittest.TestCase):
    """Tests to check the documentation and style of Permissions class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(Permissions, inspect.isfunction)

    def test_pep8_conformance_permissions(self):
        """Test that models/permissions.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/permissions.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_permissions(self):
        """Test that tests/test_models/test_permissions.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_permissions.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_permissions_module_docstring(self):
        """Test for the permissions.py module docstring"""
        self.assertIsNot(permissions.__doc__, None,
                         "permissions.py needs a docstring")
        self.assertTrue(len(permissions.__doc__) >= 1,
                        "permissions.py needs a docstring")

    def test_permissions_class_docstring(self):
        """Test for the Permissions class docstring"""
        self.assertIsNot(Permissions.__doc__, None,
                         "Permissions class needs a docstring")
        self.assertTrue(len(Permissions.__doc__) >= 1,
                        "Permissions class needs a docstring")

    def test_permissions_func_docstrings(self):
        """Test for the presence of docstrings in Permissions methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPermissions(unittest.TestCase):
    """Test the Permissions class"""
    def test_is_subclass(self):
        """Test that Permissions is a subclass of BaseModel"""
        user = Permissions()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "created_by"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "updated_by"))

    def test_first_name_attr(self):
        """Test that Permissions has attr first_name, and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "first_name"))
        if storage.storage_t == 'db':
            self.assertEqual(user.first_name, None)
        else:
            self.assertEqual(user.first_name, "")

    def test_last_name_attr(self):
        """Test that Permissions has attr last_name, and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "last_name"))
        if storage.storage_t == 'db':
            self.assertEqual(user.last_name, None)
        else:
            self.assertEqual(user.last_name, "")

    def test_gender_attr(self):
        """Test that Permissions has attr gender, and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "gender"))
        if storage.storage_t == 'db':
            self.assertEqual(user.gender, None)
        else:
            self.assertEqual(user.gender, "")

    def test_email_attr(self):
        """Test that Permissions has attr email, and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "email"))
        if storage.storage_t == 'db':
            self.assertEqual(user.email, None)
        else:
            self.assertEqual(user.email, "")

    def test_dob_attr(self):
        """Test that Permissions has attr dob, and it's 0"""
        user = Permissions()
        self.assertTrue(hasattr(user, "dob"))
        if storage.storage_t == 'db':
            self.assertEqual(user.dob, None)
        else:
            self.assertEqual(user.dob, "")

    def test_marital_status_attr(self):
        """Test that Permissions has attr marital_status,
        and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "marital_status"))
        if storage.storage_t == 'db':
            self.assertEqual(user.marital_status, None)
        else:
            self.assertEqual(user.marital_status, "")

    def test_address_attr(self):
        """Test that Permissions has attr address, and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "address"))
        if storage.storage_t == 'db':
            self.assertEqual(user.address, None)
        else:
            self.assertEqual(user.address, "")

    def test_telephone_number_attr(self):
        """Test that Permissions has attr telephone_number,
        and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "telephone_number"))
        if storage.storage_t == 'db':
            self.assertEqual(user.telephone_number, None)
        else:
            self.assertEqual(user.telephone_number, "")

    def test_kinfirst_name_attr(self):
        """Test that Permissions has attr kinfirst_name,
        and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "kinfirst_name"))
        if storage.storage_t == 'db':
            self.assertEqual(user.kinfirst_name, None)
        else:
            self.assertEqual(user.kinfirst_name, "")

    def test_kinlast_name_attr(self):
        """Test that Permissions has attr kinlast_name,
        and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "kinlast_name"))
        if storage.storage_t == 'db':
            self.assertEqual(user.kinlast_name, None)
        else:
            self.assertEqual(user.kinlast_name, "")

    def test_kincontact_address_attr(self):
        """Test that Permissions has attr kincontact_address,
        and it's an empty string"""
        user = Permissions()
        self.assertTrue(hasattr(user, "kincontact_address"))
        if storage.storage_t == 'db':
            self.assertEqual(user.kincontact_address, None)
        else:
            self.assertEqual(user.kincontact_address, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Permissions()
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
        u = Permissions()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Permissions")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        user = Permissions()
        string = "[Permissions] {}".format(user.__dict__)
        self.assertEqual(string, str(user))

if __name__ == '__main__':
    unittest.main()
