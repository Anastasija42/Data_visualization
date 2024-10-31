import unittest

from task import plot_chart
from task_solved import plot_chart as pc


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(str(plot_chart()), 'Axes(0.0706528,0.0971296;0.733278x0.840648)', msg="adds 1 + 2 to equal 3")
