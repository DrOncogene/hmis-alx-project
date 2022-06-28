#!/usr/bin/python3
"""
unittest module to test record class
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models import record
from models.staff import Staff
from tests.test_models.test_base_model import TestBaseModel
from tests.test_models.test_base_user import TestBaseUser
from tests.test_models.test_staff import TestStaff

RecordOfficer = record.RecordOfficer


class TestRecordDocs(unittest.TestCase):
    """Tests to check the documentation and style of RecordOfficer class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(record, inspect.isfunction)

    def test_pep8_conformance_record(self):
        """Test that models/record.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/record.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_record(self):
        """Test that tests/test_models/test_record.py conforms to PEP8."""
        pep8s = pep8.StyleGuide()
        result = pep8s.check_files(['tests/test_models/test_record.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_record_module_docstring(self):
        """Test for the record.py module docstring"""
        self.assertIsNot(record.__doc__, None,
                         "record.py needs a docstring")
        self.assertTrue(len(record.__doc__) >= 1,
                        "record.py needs a docstring")

    def test_recordofficer_class_docstring(self):
        """Test for the RecordOfficer class docstring"""
        self.assertIsNot(RecordOfficer.__doc__, None,
                         "RecordOfficer class needs a docstring")
        self.assertTrue(len(RecordOfficer.__doc__) >= 1,
                        "RecordOfficer class needs a docstring")

    def test_record_func_docstrings(self):
        """Test for the presence of docstrings in RecordOfficer methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestRecordOfficer(TestBaseModel, TestBaseUser, TestStaff):
    """tests the record"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.user = Staff(
            email='email',
            username='username',
            password='password'
        )
        self.user.save()
        self.tic = datetime.now()
        self.inst1 = RecordOfficer(
            email='email1',
            username='username1',
            password='password1'
        )
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = RecordOfficer(
            email='email2',
            username='username2',
            password='password2'
        )
        self.inst2.save()
        self.staff = self.user = storage.get(Staff, 'id', self.user.id)
        self.inst1 = storage.get(RecordOfficer, 'id', self.inst1.id)
        self.record = self.inst1
        self.inst2 = storage.get(RecordOfficer, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.user.delete()
        self.inst1.delete()
        self.inst2.delete()
        self.staff.delete()
        storage.save()

    def test_obj_has_attr(self):
        """check record obj for attr"""
        record = self.record
        self.assertIsInstance(record, Staff)
        self.assertTrue(hasattr(record, 'job_title'))
        self.assertEqual(record.job_title, 'RecordOfficer')
        self.assertTrue(hasattr(record, 'permissions'))


if __name__ == '__main__':
    unittest.main()
