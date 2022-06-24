#!/usr/bin/python3
"""
Contains the TestBaseNurseNoteDocs classes
"""

import inspect
import unittest
from datetime import datetime

import pep8
from storage import storage
from models.patient import Patient
from models.notes import nursenote
from tests.test_models.test_base_model import TestBaseModel

NurseNote = nursenote.NurseNote


class TestNurseNoteDocs(unittest.TestCase):
    """Tests to check the documentation and style of NurseNote class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.nursenote_f = inspect.getmembers(NurseNote, inspect.isfunction)

    def test_pep8_conformance_nursenote(self):
        """Test that models/notes/nursenote.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/notes/nursenote.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_nursenote(self):
        """Test that tests/test_models/test_notes/test_nursenote.py
        conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(
            ['tests/test_models/test_notes/test_nursenote.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_nursenote_module_docstring(self):
        """Test for the nursenote.py module docstring"""
        self.assertIsNot(nursenote.__doc__, None,
                         "nursenote.py needs a docstring")
        self.assertTrue(len(nursenote.__doc__) >= 1,
                        "nursenote.py needs a docstring")

    def test_nursenote_class_docstring(self):
        """Test for the nursenote class docstring"""
        self.assertIsNot(NurseNote.__doc__, None,
                         "NurseNote class needs a docstring")
        self.assertTrue(len(NurseNote.__doc__) >= 1,
                        "NurseNote class needs a docstring")

    def test_nursenote_func_docstrings(self):
        """Test for the presence of docstrings in nursenote methods"""
        for func in self.nursenote_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestNurseNote(TestBaseModel):
    """Test the NurseNote class"""
    def setUp(self) -> None:
        self.setUpBase()

    def tearDown(self) -> None:
        self.tearDownBase()

    def setUpBase(self):
        """sets up test object for parent test classes"""
        self.patient = Patient()
        self.patient.save()
        self.patient = storage.get(Patient, 'id', self.patient.id)
        self.tic = datetime.now()
        self.inst1 = NurseNote(pid=self.patient.pid)
        self.inst1.save()
        self.toc = datetime.now()
        self.inst2 = NurseNote(pid=self.patient.pid)
        self.inst2.save()
        self.inst1 = storage.get(NurseNote, 'id', self.inst1.id)
        self.nursenote = self.inst1
        self.inst2 = storage.get(NurseNote, 'id', self.inst2.id)

    def tearDownBase(self) -> None:
        """tearDown for parent classes"""
        self.inst1.delete()
        self.inst2.delete()
        self.patient.delete()
        storage.save()

    def test_pid_attr(self):
        """Test that NurseNote has attr pid, and it's an None"""
        self.assertTrue(hasattr(self.nursenote, "pid"))
        self.assertEqual(self.nursenote.pid, self.patient.pid)

    def test_note_attr(self):
        """Test that NurseNote has attr note, and it's an empty string"""
        self.assertTrue(hasattr(self.nursenote, "note"))
        self.assertEqual(self.nursenote.note, None)

if __name__ == '__main__':
    unittest.main()
