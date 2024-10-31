import unittest

from task import aggregate_data
from task_solved import aggregate_data as ag

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(aggregate_data().loc['PS4', 'Action'], 142, msg="Success!")
