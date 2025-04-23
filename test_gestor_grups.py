import unittest
import os
import sqlite3
from gestor_grups import crear_base_dades, intro_dades, afegir_grup, consultar_grup_per_nom

TEST_DB = "test_grups.db"

class TestGestorGrups(unittest.TestCase):

    def setUp(self):
        crear_base_dades(TEST_DB)

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_afegir_i_consultar_grup(self):
        afegir_grup("Queen", 1970, "Rock", 4, TEST_DB)
        conn = sqlite3.connect(TEST_DB)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grups WHERE nom = ?", ("Queen",))
        resultat = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[1], "Queen")
        self.assertEqual(resultat[2], 1970)
        self.assertEqual(resultat[3], "Rock")
        self.assertEqual(resultat[4], 4)

    def test_intro_dades_invalid_any(self):
        with self.assertRaises(ValueError):
            input_values = ["Beatles", "1950", "Rock", "4"]
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                intro_dades()

    def test_intro_dades_invalid_membres(self):
        with self.assertRaises(ValueError):
            input_values = ["Beatles", "1965", "Rock", "0"]
            with unittest.mock.patch('builtins.input', side_effect=input_values):
                intro_dades()

if __name__ == '__main__':
    unittest.main()
