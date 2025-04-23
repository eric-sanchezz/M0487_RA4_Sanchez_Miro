import sqlite3


def crear_base_dades(db_path="grups.db"):
    """Crea la base de dades i la taula grups si no existeixen."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            any_inici INTEGER NOT NULL,
            tipus TEXT NOT NULL,
            membres INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def intro_dades(nom=None):
    """
    Intoducció de dades per a un grup musical.
    Retorna una tupla amb (nom, any_inici, tipus, membres) després de validar-los.
    """
    if not nom:
        nom = input("Nom del grup: ").strip()
    if not nom:
        raise ValueError("El nom no pot estar buit.")

    try:
        any_inici = int(input("Any d'inici (>=1960): "))
        if any_inici < 1960:
            raise ValueError("L'any d'inici ha de ser igual o superior a 1960.")
    except ValueError:
        raise ValueError("Any d'inici invàlid. Ha de ser un enter >= 1960.")

    tipus = input("Tipus de música: ").strip()
    if not tipus:
        raise ValueError("El tipus de música no pot estar buit.")

    try:
        membres = int(input("Nombre d'integrants (>0): "))
        if membres <= 0:
            raise ValueError("El nombre d'integrants ha de ser superior a 0.")
    except ValueError:
        raise ValueError("Nombre d'integrants invàlid. Ha de ser un enter > 0.")

    return nom, any_inici, tipus, membres


def afegir_grup(nom, any_inici, tipus, membres, db_path="grups.db"):
    """Afegeix un nou grup musical a la base de dades."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grups (nom, any_inici, tipus, membres) VALUES (?, ?, ?, ?)",
                       (nom, any_inici, tipus, membres))
        conn.commit()
        print(f"Grup '{nom}' afegit correctament.")
    except Exception as e:
        print("Error en afegir grup:", e)
    finally:
        conn.close()


def eliminar_grup(nom, db_path="grups.db"):
    """Elimina un grup pel seu nom."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM grups WHERE nom = ?", (nom,))
        if cursor.rowcount == 0:
            print("No s'ha trobat cap grup amb aquest nom.")
        else:
            print("Grup eliminat correctament.")
        conn.commit()
    except Exception as e:
        print("Error en eliminar el grup:", e)
    finally:
        conn.close()


def actualitzar_grup(nom, nou_nom, nou_any, nou_tipus, nous_membres, db_path="grups.db"):
    """Actualitza les dades d’un grup musical existent."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE grups SET nom = ?, any_inici = ?, tipus = ?, membres = ?
            WHERE nom = ?
        ''', (nou_nom, nou_any, nou_tipus, nous_membres, nom))
        if cursor.rowcount == 0:
            print("No s'ha trobat cap grup amb aquest nom.")
        else:
            print("Grup actualitzat correctament.")
        conn.commit()
    except Exception as e:
        print("Error en actualitzar el grup:", e)
    finally:
        conn.close()


def mostrar_grups(db_path="grups.db"):
    """Mostra tots els grups musicals emmagatzemats."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM grups')
    grups = cursor.fetchall()
    conn.close()

    if grups:
        for grup in grups:
            print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
    else:
        print("No hi ha grups a la base de dades.")


def consultar_grup_per_nom(nom, db_path="grups.db"):
    """Consulta i mostra un grup musical pel seu nom."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups WHERE nom = ?", (nom,))
    grup = cursor.fetchone()
    conn.close()

    if grup:
        print(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
    else:
        print("No s'ha trobat cap grup amb aquest nom.")


def menu():
    crear_base_dades()
    while True:
        print("\n--- Menú ---")
        print("1. Afegir un nou grup de música")
        print("2. Mostrar tots els grups de música")
        print("3. Eliminar un grup")
        print("4. Actualitzar un grup")
        print("5. Consultar un grup per nom")
        print("0. Sortir")
        opcio = input("Tria una opció: ")

        if opcio == "1":
            try:
                nom, any_inici, tipus, membres = intro_dades()
                afegir_grup(nom, any_inici, tipus, membres)
            except ValueError as e:
                print("Error:", e)

        elif opcio == "2":
            mostrar_grups()

        elif opcio == "3":
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom)

        elif opcio == "4":
            nom = input("Nom del grup a actualitzar: ")
            try:
                nou_nom, nou_any, nou_tipus, nous_membres = intro_dades()
                actualitzar_grup(nom, nou_nom, nou_any, nou_tipus, nous_membres)
            except ValueError as e:
                print("Error:", e)

        elif opcio == "5":
            nom = input("Nom del grup a consultar: ")
            consultar_grup_per_nom(nom)

        elif opcio == "0":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torna-ho a provar.")


if __name__ == "__main__":
    menu()