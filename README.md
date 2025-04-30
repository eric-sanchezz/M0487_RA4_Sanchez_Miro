# Gestor de Grups Musicals

Aplicació de Python per a la gestió de grups musicals. Aquesta aplicació permet afegir, consultar, actualitzar i eliminar grups musicals emmagatzemats en una base de dades SQLite. El projecte es basa en una estructura clara de funcions reutilitzables i ben documentades.

## Descripció del projecte

El projecte consisteix en una aplicació que gestiona grups musicals utilitzant una base de dades SQLite. Els grups musicals poden ser afegits, actualitzats, eliminats o consultats a través d'un conjunt de funcions implementades en Python. Es fa ús de la validació de les dades d'entrada per assegurar que la informació proporcionada sigui correcta (any de creació, nombre d'integrants, tipus de música, etc.).

## Estructura del codi

- **`gestor_grups.py`**: Conté totes les funcions de l'aplicació que interactuen amb la base de dades, com ara:
  - `afegir_grup()`: Afegir un nou grup a la base de dades.
  - `consultar_grup()`: Consultar un grup per nom.
  - `actualitzar_grup()`: Actualitzar les dades d'un grup existent.
  - `eliminar_grup()`: Eliminar un grup de la base de dades.
  - `mostrar_grups()`: Llistar tots els grups enregistrats en la base de dades.
  - `intro_dades()`: Funció reutilitzable per gestionar la introducció i validació de dades dels grups musicals.
  
- **`test_gestor_grups.py`**: Conté les proves unitàries implementades amb el mòdul `unittest` per assegurar el correcte funcionament de les funcions de l'aplicació. A les proves es comprova la funcionalitat de les funcions com `afegir_grup`, `eliminar_grup`, `actualitzar_grup` i també la validació de les dades d'entrada a través de la funció `intro_dades`.

- **`grups.db`**: Fitxer SQLite on s'emmagatzemen les dades dels grups musicals. Si el fitxer no existeix, es crearà automàticament en iniciar l'aplicació.

- **`README.md`**: Aquest fitxer, que conté la documentació del projecte, la qual proporciona informació sobre la seva estructura, funcionament i ús.

- **`HISTÒRIC.md`**: Registre de canvis realitzats pel grup de desenvolupament, seguint la metodologia de treball col·laborativa amb GitHub. Aquest fitxer documenta els canvis i les tasques realitzades per cada membre del projecte.

## Instruccions d'ús

Per executar l'aplicació, executarem el fitxer test_gestor_grups.py per comprovar que els mètodes funcionen correctament. Per executar el programa principal, haurem d'anar al fitxer gestor_grups.py i donar-li a executar, on s'obrirà el menú i podrem fer servir el programa.

## Crèdits i autoria 

Programa fet per Èric Sánchez i Héctor Miró