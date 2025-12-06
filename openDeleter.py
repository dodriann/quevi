import os
from nfo import information


class OpenDeleter:

    def __init__(self):
        # NFO-Informationen des Programmes
        self.nfo = information(
            "OpenDeleter",
            "Löscht Dateien über die jetOS Shell.",
            "Dorian Riazy",
            "version 1.0.0",
            "jetOS Alpine"
        )

        # Geschützte Dateien/Ordner
        self.protected = [
            "sll_shell.py",
            "cinter.py",
            "openDeleter.py",
            "jetlauncher.py",
            "vm.py",
            "bscript.py"
        ]

    # ---------------------------------------------------------
    # Prüft, ob Datei gelöscht werden darf
    # ---------------------------------------------------------
    def is_protected(self, path):
        name = os.path.basename(path)
        return name in self.protected

    # ---------------------------------------------------------
    # Datei löschen
    # ---------------------------------------------------------
    def delete(self, path):
        path = path.strip()

        # Existenz prüfen
        if not os.path.exists(path):
            print(f"OpenDeleter: Datei nicht gefunden → {path}")
            return False

        # Schutzsystem
        if self.is_protected(path):
            print(f"OpenDeleter: '{path}' ist geschützt und kann nicht gelöscht werden.")
            return False

        try:
            os.remove(path)
            print(f"[OK] Datei gelöscht: {path}")
            return True
        except Exception as e:
            print(f"[ERROR] Konnte Datei nicht löschen ({e})")
            return False

    # ---------------------------------------------------------
    # Ausgabe eines Hilfe-Menüs
    # ---------------------------------------------------------
    def help(self):
        print("""
OpenDeleter – jetOS Datei-Löschsystem
------------------------------------
del -f <datei>     → Löscht eine Datei
del -h             → Zeigt dieses Hilfe-Menü
""")


# ==========================================================
# Wenn Programm direkt gestartet wird (Standalone-Modus)
# ==========================================================
if __name__ == "__main__":
    deleter = OpenDeleter()

    while True:
        cmd = input("OpenDeleter > ").strip()

        if cmd == "exit":
            break

        if cmd.startswith("del "):
            path = cmd.replace("del ", "")
            deleter.delete(path)

        elif cmd == "help" or cmd == "-h":
            deleter.help()

        else:
            print("Unbekannter Befehl. Nutze: help")
