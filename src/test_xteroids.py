import unittest
import movni

class TestMovni(unittest.TestCase):
    def test_puntomedio(self):
        self.assertEqual(movni.puntomedio((1, 1), (5, 5)), (3, 3))

if __name__ == "__main__":
    unittest.main()
