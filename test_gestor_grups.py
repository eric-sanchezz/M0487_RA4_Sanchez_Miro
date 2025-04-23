import unittest
import sqlite3
import os
from tempfile import TemporaryDirectory
from gestor_grups import afegir_grup, eliminar_grup, actualitzar_grup, mostrar_grups, crear_base_dades

class TestGrupsMusicals(unittest.TestCase):
    def setUp(self):
        # Crea una base de dades temporal per als tests
        self.temp_dir = TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "grups_musica.db")
        crear_base_dades(self.db_path)

    def tearDown(self):
        # Elimina la base de dades temporal després de cada test
        self.temp_dir.cleanup()

    def test_afegir_grup(self):
        # Afegir un grup i comprovar que es troba a la base de dades
        afegir_grup("Mishima", 2000, "Indie", 5, self.db_path)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grups WHERE nom = 'Mishima'")
        resultat = cursor.fetchall()
        conn.close()
        self.assertEqual(len(resultat), 1)

    def test_eliminar_grup(self):
        # Afegir un grup i després eliminar-lo, comprovant que ja no existeix
        afegir_grup("Sopa de Cabra", 1986, "Rock", 4, self.db_path)
        eliminar_grup("Sopa de Cabra", self.db_path)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grups WHERE nom = 'Sopa de Cabra'")
        resultat = cursor.fetchall()
        conn.close()
        self.assertEqual(len(resultat), 0)

    def test_actualitzar_grup(self):
        # Afegir un grup i després actualitzar les seves dades
        afegir_grup("Mishima", 2000, "Indie", 5, self.db_path)
        actualitzar_grup("Mishima", "Mishima 2", 2005, "Pop", 6, self.db_path)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM grups WHERE nom = 'Mishima 2'")
        resultat = cursor.fetchall()
        conn.close()
        self.assertEqual(len(resultat), 1)
        self.assertEqual(resultat[0][1], "Mishima 2")
        self.assertEqual(resultat[0][2], 2005)
        self.assertEqual(resultat[0][3], "Pop")
        self.assertEqual(resultat[0][4], 6)

if __name__ == '__main__':
    unittest.main()
