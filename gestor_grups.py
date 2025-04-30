import logging
import sqlite3
import os

logging.basicConfig(level=logging.INFO)

def crear_base_dades(db_path):
    """
    Aquesta funció crea la base de dades amb la taula 'grups' si no existeix.
    La taula conté les següents columnes:
    - id: Identificador únic per cada grup (clau primària).
    - nom: Nom del grup musical.
    - any_inici: Any de creació del grup.
    - tipus: Tipus de música del grup (amb restricció per 'pop', 'trap', 'rap').
    - integrants: Nombre d'integrants del grup.
    """
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS grups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                any_inici INTEGER,
                tipus TEXT CHECK(tipus IN ('pop', 'trap', 'rap')),
                integrants INTEGER
            )
        """)
        conn.commit()
        conn.close()

def validar_tipus(tipus):
    """
    Aquesta funció valida que el tipus de música sigui un valor permès: 'pop', 'trap' o 'rap'.
    Si no és vàlid, mostra un missatge per terminal i retorna False.
    """
    if tipus not in ('pop', 'trap', 'rap'):
        print("El tipus de música ha de ser 'pop', 'trap' o 'rap'. Intenta-ho de nou.")
        return False
    return True

def validar_any_inici(any_inici):
    """
    Aquesta funció valida que l'any d'inici sigui més gran que 1960.
    """
    if any_inici <= 1960:
        print("L'any d'inici ha de ser posterior a 1960. Intenta-ho de nou.")
        return False
    return True

def afegir_grup(nom, any_inici, tipus, integrants, db_path):
    """
    Aquesta funció afegeix un grup a la base de dades amb els següents paràmetres:
    - nom: Nom del grup musical.
    - any_inici: Any de creació del grup.
    - tipus: Tipus de música (pop, trap, rap).
    - integrants: Nombre d'integrants del grup.
    
    Després d'afegir el grup, s'afegeix un registre de log per confirmar-ho.
    """
    if not validar_tipus(tipus) or not validar_any_inici(any_inici):
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO grups (nom, any_inici, tipus, integrants)
        VALUES (?, ?, ?, ?)
    """, (nom, any_inici, tipus, integrants))
    conn.commit()
    conn.close()
    logging.info(f"Grup '{nom}' afegit correctament.")

def eliminar_grup(nom, db_path):
    """
    Aquesta funció elimina un grup de la base de dades mitjançant el seu nom.
    
    Després d'eliminar el grup, s'afegeix un registre de log per confirmar-ho.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM grups WHERE nom = ?", (nom,))
    conn.commit()
    conn.close()
    logging.info(f"Grup '{nom}' eliminat correctament.")

def actualitzar_grup(nom_antiga, nom_nova, any_inici, tipus, integrants, db_path):
    """
    Aquesta funció actualitza la informació d'un grup existent a la base de dades.
    Els paràmetres per actualitzar són:
    - nom_antiga: Nom original del grup a actualitzar.
    - nom_nova: Nou nom del grup.
    - any_inici: Nou any de creació.
    - tipus: Nou tipus de música.
    - integrants: Nou nombre d'integrants.
    
    Un cop actualitzat el grup, s'afegeix un registre de log per confirmar-ho.
    """
    if not validar_tipus(tipus) or not validar_any_inici(any_inici):
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE grups 
        SET nom = ?, any_inici = ?, tipus = ?, integrants = ? 
        WHERE nom = ?
    """, (nom_nova, any_inici, tipus, integrants, nom_antiga))
    conn.commit()
    conn.close()
    logging.info(f"Grup '{nom_antiga}' actualitzat correctament.")

def mostrar_grups(db_path):
    """
    Aquesta funció mostra tots els grups musicals emmagatzemats a la base de dades.
    Utilitza el registre de logs per mostrar la informació de cada grup:
    - ID
    - Nom
    - Any de creació
    - Tipus de música
    - Nombre d'integrants
    
    Aquesta informació es mostrarà mitjançant un registre de log de nivell INFO.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM grups")
    grups = cursor.fetchall()
    for grup in grups:
        logging.info(f"ID: {grup[0]}, Nom: {grup[1]}, Any inici: {grup[2]}, Tipus: {grup[3]}, Integrants: {grup[4]}")
    conn.close()

def mostrar_menu():
    """
    Aquesta funció mostra el menú principal amb les opcions disponibles.
    """
    print("\nGestió de Grups Musicals")
    print("1. Afegir un grup")
    print("2. Eliminar un grup")
    print("3. Actualitzar un grup")
    print("4. Mostrar tots els grups")
    print("5. Sortir")

def main():
    """
    Aquesta funció és el punt d'entrada per executar el programa amb un menú interactiu.
    """
    db_path = "grups_musica.db"
    crear_base_dades(db_path)
    
    while True:
        mostrar_menu()
        opcio = input("Escull una opció: ")

        if opcio == '1':
            nom = input("Nom del grup: ")
            any_inici = int(input("Any d'inici: "))
            while True:
                tipus = input("Tipus de música (pop, trap, rap): ")
                if validar_tipus(tipus):
                    break
            integrants = int(input("Nombre d'integrants: "))
            afegir_grup(nom, any_inici, tipus, integrants, db_path)
        
        elif opcio == '2':
            nom = input("Nom del grup a eliminar: ")
            eliminar_grup(nom, db_path)
        
        elif opcio == '3':
            nom_antiga = input("Nom del grup a actualitzar: ")
            nom_nova = input("Nou nom del grup: ")
            any_inici = int(input("Nou any d'inici: "))
            while True:
                tipus = input("Nou tipus de música (pop, trap, rap): ")
                if validar_tipus(tipus):
                    break
            integrants = int(input("Nou nombre d'integrants: "))
            actualitzar_grup(nom_antiga, nom_nova, any_inici, tipus, integrants, db_path)
        
        elif opcio == '4':
            mostrar_grups(db_path)
        
        elif opcio == '5':
            print("Fins aviat!")
            break
        
        else:
            print("Opció no vàlida, torna a intentar-ho.")

if __name__ == '__main__':
    main()
