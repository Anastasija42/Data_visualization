import unittest
import matplotlib
import pandas

try:
    class TestCase(unittest.TestCase):
        def test_add(self):
            print("Matplotlib and Pandas are successfully installed.")

except ImportError as e:
    print(f"Error: {e}. Please ensure both matplotlib and pandas are installed.")