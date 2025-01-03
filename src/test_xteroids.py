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
        ovniA = movni.Meteoro((500, 250), 0, (0, 0), movni.catmet[1][1], 50, 30, 0, 1)
        ovniA.puntos = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
        ovniA.lineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
        ovniA.rotar(0)

        ovniB = movni.Meteoro((600, 300), 0, (0, 0), movni.catmet[1][1], 50, 30, 0, 1)
        ovniB.puntos = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
        ovniB.lineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
        ovniB.rotar(0)

        self.assertTrue(movni.sesolapan(ovniA, ovniB))

    def test_pendiente(self):
        self.assertEqual(movni.pendiente((1, 0), (2, 1)), 1)
        self.assertEqual(movni.pendiente((1, 1), (2, 0)), -1)
        self.assertEqual(movni.pendiente((1, 1), (2, 1)), 0)
        self.assertEqual(movni.pendiente((1, 0), (1, 1)), None)

    def test_secruzan(self):
        self.assertEqual(movni.secruzan((1, 0), (3, 2), (1, 2), (3, 0)), (2, 1))
        self.assertEqual(movni.secruzan((1, 0), (2, 2), (3, 0), (4, 2)), None)
        self.assertEqual(movni.secruzan((1, 1), (5, 1), (4, 0), (4, 5)), (4, 1))

    def test_distancia(self):
        self.assertEqual(movni.distancia((1, 1), (2, 1)), 1)
        self.assertEqual(movni.distancia((1, 0), (-5, 0)), 6)
        self.assertEqual(movni.distancia((1, 1), (1, 5)), 4)

    def test_baleado(self):
        meteoro = movni.Meteoro((600, 300), 0, (0, 0), movni.catmet[1][1], 50, 30, 0, 1)
        meteoro.puntos = [(-150, -150), (150, -150), (150, 150), (-150, 150)]
        meteoro.lineas = [(0, 1), (1, 2), (2, 3), (3, 0)]
        meteoro.rotar(0)

        bala = movni.Bala((456, 300), 0, (1, 0), movni.catmet[1][1], movni.catmet[0][1], 50, 360)

        choqueD = movni.Choque(meteoro, bala, (450, 300), ((-150, 150), (-150, -150)))

        choqueO = movni.baleado(meteoro, bala)

        self.assertEqual(choqueO.ovniA, choqueD.ovniA)
        self.assertEqual(choqueO.ovniB, choqueD.ovniB)
        self.assertEqual(choqueO.punto, choqueD.punto)
        self.assertEqual(choqueO.plano, choqueD.plano)

    def test_puntomedio(self):
        self.assertEqual(movni.puntomedio((1, 1), (5, 5)), (3, 3))

if __name__ == "__main__":
    unittest.main()

# Local Variables:
# compile-command: "python3 test_xteroids.py"
# End:
