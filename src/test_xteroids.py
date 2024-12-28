import unittest
import movni

class TestMovni(unittest.TestCase):

    def test_estaentre(self):
        self.assertTrue(movni.estaentre(5, 1, 7))
        self.assertTrue(movni.estaentre(6, 10, 6))

    def test_puntoestaentre(self):
        self.assertTrue(movni.puntoestaentre((5, 5), (0,0), (10, 10)))
        self.assertTrue(movni.puntoestaentre((1, 5), (10, 5), (0,5)))

    def test_sesolapandim(self):
        self.assertTrue(movni.sesolapadim(1, 5, 4, 8))
        self.assertTrue(movni.sesolapadim(2, 7, 7, 14))
        self.assertFalse(movni.sesolapadim(5, 8, 10, 15))
        self.assertFalse(movni.sesolapadim(-1, -5, 1, 5))
        self.assertTrue(movni.sesolapadim(-4, 1, 5, -1))

    def test_sesolapan(self):
        color = (255, 54, 59)
        ovniA = movni.Meteoro((500, 250), 0, (0, 0), color, 50, 30, 0, 1)
        ovniA.puntos = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
        ovniA.lineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
        ovniA.rotar(0)

        ovniB = movni.Meteoro((600, 300), 0, (0, 0), color, 50, 30, 0, 1)
        ovniB.puntos = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
        ovniB.lineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
        ovniB.rotar(0)

        self.assertTrue(movni.sesolapan(ovniA, ovniB))

    def test_pendiente(self):
        self.assertEqual(movni.pendiente((1, 0), (2, 1)), 1)

    def test_puntomedio(self):
        self.assertEqual(movni.puntomedio((1, 1), (5, 5)), (3, 3))

if __name__ == "__main__":
    unittest.main()

# Local Variables:
# compile-command: "python3 test_xteroids.py"
# End:
