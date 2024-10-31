import unittest

from task import load_data
from task_solved import load_data as ld

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(load_data(), 0, msg="Task done successfully!")
