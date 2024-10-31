import unittest

from task import filter_data
from task_solved import filter_data as fd

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(filter_data(), 829, msg="Nice!")
