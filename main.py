import json

# Einrichtung der Liste, die die Datensätze der Spiele speichert
spielekiste = []

# Die Tuple-Liste, mit der Auswahl der Systeme
systeme = {
    1: "C64",
    2: "NES",
    3: "SNES",
    4: "Gameboy",
    5: "Gameboy Colour",
    6: "Gameboy Advance",
    7: "Amiga",
    8: "Atari ST",
    9: "Atari VCS (2600)",
    10: "PC / MS-DOS",
    11: "SEGA Megadrive / Genesis",
    12: "Famicom",
    13: "Sony Playstation 1",
    14: "Sony Playstation 2",
    15: "PC / Schneider Amstrad 1512 DD",
    16: "Tandy TRS-80, Model 1",
    17: "Texas Instruments TI-99/4A",
    18: "Sonstige\n" }


# Medium-Auswahl
medium = {
    1: "Diskette",
    2: "Cartridge",
    3: "CD-/DVD-ROM",
    4: "ISO-Image",
    5: "Disketten-Image",
    6: "Download\n" }

#=====================================================FUNKTIONEN=====================================================

# Erstellung der json-Datei und Sicherung der Eingaben
def save_game():
    with open("spielekiste.json", "w", encoding="utf-8") as file:
        json.dump(spielekiste, file, indent=4, ensure_ascii=False)

# Laden der json-Datei beim Start des Programms
def load_games():
    global spielekiste
    try:
        with open("spielekiste.json", "r", encoding="utf-8") as file:
            spielekiste = json.load(file)
    except FileNotFoundError:
        spielekiste = []
        spiel_hinzufuegen()
    except json.JSONDecodeError:
        print("Fehler beim Laden der Archivdatei. Die Datei ist möglicherweise beschädigt.")
        return
            
#Einträge wieder entfernen            
def eintrag_loeschen():
    
    if not spielekiste:
        print("\nDie Liste ist noch leer.")
        return
    
    print("\n--- Spiel löschen ---") 

    try:
        
        for index, game in enumerate(spielekiste):
                    print(f"{index+1} : {game} ")


        auswahl = int(input("\n Welches Spiel möchtest du löschen? (Bitte Nummer eingeben):"))
        if auswahl == 0:
         return

        #Gültigkeit der Nummer überprüfen
        if 0 <= index < len(spielekiste):
            gelöscht = spielekiste.pop(index)
            print(f"'{gelöscht['name']}' wurde erfolgreich gelöscht.")
            save_game()
        else: 
            print("Diese Nummer ist ungültig. Bitte versuche es noch einmal: ")
            eintrag_loeschen()

    except ValueError:
        print("Gib bitte eine Zahl ein.!")

            
                                
# Eingabe des Spiels und Speicherung in json-Datei
def spiel_hinzufuegen():
    print("\n--- Neues Spiel hinzufügen ---")
    
    # Eingabe der Daten
    for nummer, modell in systeme.items():
        print(f"{nummer}: {modell}")

    wahl = int(input("Wähle das System für das Spiel aus (Bitte Nummer eingeben): "))

    if wahl in systeme:
        system = systeme[wahl]
    else:
        print("""Ungültige Auswahl. 
              Das Spiel kann so nicht gespeichert werden. 
              Bitte versuche es noch einmal!""")
        return
   

    for schluessel, geraet in medium.items():
        print(f"{schluessel}: {geraet}")

    auswahl_medium = int(input("Wähle das Medium für das Spiel aus (Bitte Nummer eingeben): "))

    if auswahl_medium in medium:
        media_wahl = medium[auswahl_medium]
    else:
        print("""Ungültige Auswahl. 
              Das Spiel kann so nicht gespeichert werden. 
              Bitte versuche es noch einmal!""")
        return

    name = input("Name des Spiels: ")       
    jahr = int(input("Erscheinungsjahr (xxxx): "))
    kommentar = input("Kurzer Kommentar: ")

    # Ein Dictionary erstellen und der Liste hinzufügen 
    spielekiste.append({
        "name": name,
        "system": system,
        "medium": media_wahl,
        "jahr": jahr,
        "kommentar": kommentar
    })
    save_game()
    print(f"'{name}' wurde erfolgreich hinzugefügt!")




def sammlung_anzeigen():
    if not spielekiste:
        print("\nDie Liste ist noch leer.")
        return

    print("\n--- Deine Retro-Sammlung ---")
    # List Comprehension: Gespeicherte Daten werden aufgelistet
    display_list = [f"{g['name']} ({g['system']}) - {g['medium']} - {g['jahr']}" for g in spielekiste]
    
    for entry in display_list:
        print(f" -   {entry}")


def statistik():
   # Anzahl der Spiele
    anzahl = len(spielekiste)
    if anzahl == 0:
        print("\nKeine Daten für Statistiken vorhanden.")
        return
    
    menge_pro_system = {}
    for game in spielekiste:
        system = game['system']
        menge_pro_system[system] = menge_pro_system.get(system, 0) + 1

    # Statistiken anzeigen lassen   
    print(f"\n----Statistiken----")
    print(f"Gesamtanzahl der Spiele: {anzahl} Spiele sind aktuell gelistet.")
    print("Anzahl Spiele je System: ")
    for system, anzahl in menge_pro_system.items():
        print(f"{system} : {anzahl} Spiele")



# Die Hauptmenü-Funktion
def main_menu():

    load_games()

    while True:
        print("\n--- RETRO-GAME-MANAGER ---")
        print("1. Spiel hinzufügen")
        print("2. Sammlung anzeigen")
        print("3. Statistiken zeigen")
        print("4. Eintrag löschen")
        print("5. Programm beenden\n")
        
        wahl = input("Was möchtest du tun? ")

        if wahl == "1":
            spiel_hinzufuegen()
        elif wahl == "2":
            sammlung_anzeigen()
        elif wahl == "3":
            statistik()
        elif wahl == "4":
            eintrag_loeschen()
        elif wahl == "5":
            print("\nTschüss! Viel Spaß beim Zocken.")
            break
        else:
            print("\nUngültige Eingabe, bitte versuche es erneut.")

# Programm starten
if __name__ == "__main__":
    main_menu()