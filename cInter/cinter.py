import os
import urllib.request
from nfo import information


class cInter:

    def __init__(self):
        # NFO System des Programmes
        self.nfo = information(
            "cInter",
            "Internet Paket Manager für jetOS.\nKann Programme installieren und GitHub-Dateien laden.",
            "Dorian Riazy",
            "version 1.0.0",
            "jetOS Alpine"
        )

        # Basis für Downloads
        self.base = "https://raw.githubusercontent.com/<REPO_URL>/"

        # Download-Ordner
        self.download_root = "cInter_packages"
        if not os.path.exists(self.download_root):
            os.makedirs(self.download_root)


    # -------------------------------------------------------------
    # GitHub Datei herunterladen
    # -------------------------------------------------------------
    def download(self, url_path, save_as):
        full_url = self.base + url_path
        local_path = os.path.join(self.download_root, save_as)

        try:
            print(f"[cInter] Lade herunter: {save_as}")
            urllib.request.urlretrieve(full_url, local_path)
            print(f"[OK] Datei gespeichert unter: {local_path}")
            return True
        except Exception as e:
            print("[cInter ERROR]", e)
            return False


    # -------------------------------------------------------------
    # Installation: OpenDeleter
    # -------------------------------------------------------------
    def install_OpenDeleter(self):
        print("\n--- Installiere OpenDeleter ---")
        return self.download(
            "OpenDeleter/openDeleter.py",
            "openDeleter.py"
        )


    # -------------------------------------------------------------
    # Installation: OpenBscript (VM, Lexer, Parser usw.)
    # -------------------------------------------------------------
    def install_OpenBscript(self):
        print("\n--- Installiere OpenBscript ---")

        files = {
            "lexer.py":   "OpenBscript/lexer.py",
            "parser.py":  "OpenBscript/parser.py",
            "vm.py":      "OpenBscript/vm.py",
            "codegen.py": "OpenBscript/codegen.py",
            "builder.py": "OpenBscript/builder.py",
            "bscript.py": "OpenBscript/bscript.py"
        }

        ok = True
        for out, url in files.items():
            if not self.download(url, out):
                ok = False

        return ok


    # -------------------------------------------------------------
    # Installation: JetLauncher
    # -------------------------------------------------------------
    def install_JetLauncher(self):
        print("\n--- Installiere JetLauncher ---")

        launcher_code = """
import os
import subprocess

print("JetLauncher 1.0 -- jetOS Alpine")

while True:
    cmd = input("jl > ")

    if cmd == "exit":
        break

    if cmd.startswith("run "):
        target = cmd.replace("run ", "").strip()
        if os.path.exists(target):
            print("Starte:", target)
            subprocess.Popen(target, shell=True)
        else:
            print("Datei nicht gefunden:", target)
    else:
        print("Unbekannter JetLauncher Befehl.")
"""

        path = os.path.join(self.download_root, "jetlauncher.py")
        with open(path, "w", encoding="utf-8") as f:
            f.write(launcher_code)

        print("[OK] JetLauncher installiert")
        return True


    # -------------------------------------------------------------
    # Einstiegspunkt für Shell
    # -------------------------------------------------------------
    def install(self, package):
        package = package.lower()

        if package == "opendeleter":
            return self.install_OpenDeleter()

        elif package == "openbscript":
            return self.install_OpenBscript()

        elif package == "jetlauncher":
            return self.install_JetLauncher()

        else:
            print("cInter: Paket nicht bekannt →", package)
            return False
