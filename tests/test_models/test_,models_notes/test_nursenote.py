#!/usr/bin/python3
"""
Contains the TestBaseNurseNoteDocs classes
"""

from datetime import datetime
import inspect
from models.base_model import BaseModel
from models.notes import nursenote
import pep8
import storage
import unittest
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
        """Test that tests/test_models/est_models_notes/test_nursenote.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_models_notes/test_nursenote.py'])
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


class TestNurseNote(unittest.TestCase):
    """Test the NurseNote class"""
    def test_is_subclass(self):
        """Test that NurseNote is a subclass of BaseModel"""
        nursenote = NurseNote()
        self.assertIsInstance(nursenote, BaseModel)
        self.assertTrue(hasattr(nursenote, "id"))
        self.assertTrue(hasattr(nursenote, "created_at"))
        self.assertTrue(hasattr(nursenote, "created_by"))
        self.assertTrue(hasattr(nursenote, "updated_at"))
        self.assertTrue(hasattr(nursenote, "updated_by"))

    def test_pid_attr(self):
        """Test that NurseNote has attr pid, and it's an empty string"""
        nursenote = NurseNote()
        self.assertTrue(hasattr(nursenote, "pid"))
        if storage.storage_t == 'db':
            self.assertEqual(nursenote.pid, None)
        else:
            self.assertEqual(nursenote.pid, "")

    def test_vital_ids_attr(self):
        """Test that NurseNote has attr vital_ids, and it's a list"""
        nursenote = NurseNote()
        self.assertTrue(hasattr(nursenote, "vital_ids"))
        if storage.storage_t == 'db':
            self.assertEqual(nursenote.vital_ids, None)
        else:
            self.assertEqual(nursenote.vital_ids, [])

    def test_note_attr(self):
        """Test that NurseNote has attr note, and it's an empty string"""
        nursenote = NurseNote()
        self.assertTrue(hasattr(nursenote, "note"))
        if storage.storage_t == 'db':
            self.assertEqual(nursenote.note, None)
        else:
            self.assertEqual(nursenote.note, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = NurseNote()
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
        u = NurseNote()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "NurseNote")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        nursenote = NurseNote()
        string = "[NurseNote] {}".format(nursenote.__dict__)
        self.assertEqual(string, str(nursenote))

if __name__ == '__main__':
    unittest.main()
