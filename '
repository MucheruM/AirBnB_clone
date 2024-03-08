#!/usr/bin/python3
""" Unit test BaseModel"""

import unittest
import models
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for class BaseModel """

    def test_docstring(self):
        """ test if function, classes, methods
        and modules have the documentation string"""
        msg = "Module does not have docstring"
        self.assertIsNotNone(models.base_model.__doc__, msg)
        msg = "Class does not have docstring"
        self.assertIsNotNone(BaseModel.__doc__, msg)

    def test_executable_file(self):
        """test if file has permissions u+x to excute"""
        # Check for read access
        is_read_true = os.access("models/base_model.py", os.R_OK)
        self.assertTrue(is_read_true)
        # Checks for write access
        is_write_true = os.access("models/base_model.py", os.W_OK)
        self.assertTrue(is_write_true)
        # Checks for execute access
        is_execute_true = os.access("models/base_model.py", os.X_OK)
        self.assertTrue(is_execute_true)

    def test_init_basemodel(self):
        """ test if an object is of type BaseModel"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_id(self):
        """ test that id is unique"""
        pass

    def test_str(self):
        """check if the output of str is in the specified format"""
        pass


if __name__ == "__main__":
    unittest.main()
