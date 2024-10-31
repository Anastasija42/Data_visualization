import unittest

from task import plot_chart
from task_solved import plot_chart as pc

class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(plot_chart(), 0, msg="That's it!")
