# Einrichtung der Liste, die die Datensätze der Spiele speichert
game_library = []

def add_game():
    print("\n--- Neues Spiel hinzufügen ---")
    # Eingabe der Daten
    name = input("Name des Spiels: ")
    system = input("System (z.B. C64, NES, Amiga): ")
    
    print("Medium: 1: Diskette, 2: Cartridge, 3: CD, 4: ISO, 5: Download")
    media_types = ["Diskette", "Cartridge", "CD", "ISO", "Download"]
    media_wahl = int(input("Wähle eine Nummer: ")) - 1
    medium = media_types[media_wahl]
    
    jahr = int(input("Erscheinungsjahr: "))
    kommentar = input("Kurzer Kommentar: ")

    # Ein Dictionary erstellen und der Liste hinzufügen (.append)
    game_library.append({
        "name": name,
        "system": system,
        "medium": medium,
        "jahr": jahr,
        "kommentar": kommentar
    })
    print(f"'{name}' wurde erfolgreich hinzugefügt!")

def show_library():
    if not game_library:
        print("\nDie Liste ist noch leer.")
        return

    print("\n--- Deine Retro-Sammlung ---")
    # List Comprehension: Erstellt eine Liste von formatierten Strings
    display_list = [f"{g['name']} ({g['system']}) - {g['medium']} - {g['jahr']}" for g in game_library]
    
    for entry in display_list:
        print(f"- {entry}")

def show_stats():
    # Beispiel für die Verwendung von total (Summe) und Berechnungen
    anzahl = len(game_library)
    if anzahl == 0:
        print("\nKeine Daten für Statistiken vorhanden.")
        return

    # Berechnung des Durchschnittsalters (List Comprehension + sum)
    jahre = [g['jahr'] for g in game_library]
    durchschnitt_jahr = sum(jahre) / anzahl
    
    print(f"\n--- Statistiken ---")
    print(f"Gesamtanzahl der Spiele: {anzahl}")
    print(f"Durchschnittliches Erscheinungsjahr: {int(durchschnitt_jahr)}")

def main_menu():
    while True:
        print("\n--- RETRO-GAME-MANAGER ---")
        print("1. Spiel hinzufügen")
        print("2. Sammlung anzeigen")
        print("3. Statistiken zeigen")
        print("4. Programm beenden")
        
        wahl = input("Was möchtest du tun? ")

        if wahl == "1":
            add_game()
        elif wahl == "2":
            show_library()
        elif wahl == "3":
            show_stats()
        elif wahl == "4":
            print("Tschüss! Viel Spaß beim Zocken.")
            break
        else:
            print("Ungültige Eingabe, bitte versuche es erneut.")

# Programm starten
if __name__ == "__main__":
    main_menu()