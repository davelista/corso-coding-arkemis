#!/usr/bin/env python3
"""
check_setup.py — Corso intensivo di coding · Arkemis

Verifica che l'ambiente di lavoro sia pronto per il corso.
Usa solo la libreria standard di Python: non serve installare niente.

Uso:
    python3 check_setup.py            # controlla tutto, database "prova"
    python3 check_setup.py --db nome  # usa un altro database di prova

Esito: una riga [OK] / [KO] / [!!] per ogni strumento.
Codice di uscita 0 se tutti i controlli principali sono OK, 1 altrimenti.
"""

from __future__ import annotations

import argparse
import getpass
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Requisiti minimi
# ---------------------------------------------------------------------------
PYTHON_MIN = (3, 12)
NODE_MIN_MAJOR = 20
TIMEOUT = 20  # secondi per ogni comando esterno


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
USE_COLOR = sys.stdout.isatty() and os.name != "nt"
GREEN, RED, YELLOW, GREY, BOLD, RESET = (
    ("\033[32m", "\033[31m", "\033[33m", "\033[90m", "\033[1m", "\033[0m")
    if USE_COLOR
    else ("", "", "", "", "", "")
)


@dataclass
class Result:
    name: str
    status: str  # "OK", "KO", "!!"
    detail: str = ""
    hints: list[str] = field(default_factory=list)
    required: bool = True

    def print(self) -> None:
        color = {"OK": GREEN, "KO": RED, "!!": YELLOW}[self.status]
        line = f"{color}[{self.status}]{RESET} {BOLD}{self.name}{RESET}"
        if self.detail:
            line += f" · {self.detail}"
        print(line)
        for hint in self.hints:
            print(f"     {GREY}→ {hint}{RESET}")


def run(cmd: list[str], timeout: int = TIMEOUT) -> tuple[int, str]:
    """Esegue un comando e restituisce (codice di uscita, output unito)."""
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            stdin=subprocess.DEVNULL,
        )
        return proc.returncode, (proc.stdout + proc.stderr).strip()
    except FileNotFoundError:
        return 127, "comando non trovato"
    except subprocess.TimeoutExpired:
        return 124, f"nessuna risposta entro {timeout} secondi"


def first_version(text: str) -> str:
    match = re.search(r"\d+(\.\d+)+", text)
    return match.group(0) if match else "versione sconosciuta"


# ---------------------------------------------------------------------------
# Sistema operativo
# ---------------------------------------------------------------------------
def detect_os() -> str:
    system = platform.system()
    if system == "Darwin":
        return "mac"
    if system == "Windows":
        return "windows"
    if system == "Linux":
        release = platform.release().lower()
        if "microsoft" in release or "wsl" in release:
            return "wsl"
        return "linux"
    return "altro"


OS_LABEL = {
    "mac": "macOS",
    "wsl": "Ubuntu su WSL (Windows)",
    "linux": "Linux",
    "windows": "Windows (fuori da WSL)",
    "altro": "sistema non riconosciuto",
}


def install_hint(os_name: str, mac: str, apt: str) -> str:
    return mac if os_name == "mac" else apt


# ---------------------------------------------------------------------------
# Controlli
# ---------------------------------------------------------------------------
def check_git(os_name: str) -> list[Result]:
    if not shutil.which("git"):
        return [Result("git", "KO", "non trovato", [
            install_hint(os_name, "brew install git", "sudo apt update && sudo apt install git"),
        ])]

    _, out = run(["git", "--version"])
    results = [Result("git", "OK", first_version(out))]

    _, name = run(["git", "config", "--global", "user.name"])
    _, email = run(["git", "config", "--global", "user.email"])
    missing = []
    if not name or "non trovato" in name:
        missing.append('git config --global user.name "Nome Cognome"')
    if not email or "non trovato" in email:
        missing.append('git config --global user.email "email-di-github"')
    if missing:
        results.append(Result("git config", "KO", "nome o email mancanti", missing))
    else:
        results.append(Result("git config", "OK", f"{name} <{email}>"))

    _, branch = run(["git", "config", "--global", "init.defaultBranch"])
    if branch.strip() != "main":
        results.append(Result(
            "git branch predefinito", "!!", branch.strip() or "non impostato",
            ["git config --global init.defaultBranch main"], required=False,
        ))
    return results


def check_vscode(os_name: str) -> Result:
    if not shutil.which("code"):
        hints = ["Installa VS Code da code.visualstudio.com"]
        if os_name == "mac":
            hints.append("In VS Code: Cmd+Shift+P → «Shell Command: Install 'code' command in PATH»")
        elif os_name == "wsl":
            hints.append("Installa VS Code su Windows con l'estensione WSL, poi riapri il terminale di Ubuntu")
        return Result("vs code", "KO", "comando code non trovato", hints)
    code, out = run(["code", "--version"])
    if code != 0:
        return Result("vs code", "!!", "comando presente ma non risponde",
                      ["Riapri il terminale e riprova"], required=False)
    return Result("vs code", "OK", out.splitlines()[0] if out else "")


def check_python(os_name: str) -> list[Result]:
    version = sys.version_info
    label = f"{version.major}.{version.minor}.{version.micro}"
    results: list[Result] = []
    if (version.major, version.minor) < PYTHON_MIN:
        results.append(Result(
            "python", "KO", f"{label}, serve {PYTHON_MIN[0]}.{PYTHON_MIN[1]} o superiore",
            (["Hai già python3.12: lancia lo script con python3.12 check_setup.py"]
             if shutil.which("python3.12")
             else [install_hint(os_name, "brew install python@3.12", "Vedi la checklist della tua stanza: versione di Python troppo vecchia")]),
        ))
    else:
        results.append(Result("python", "OK", label))

    # Prova reale: crea un ambiente virtuale in una cartella temporanea.
    with tempfile.TemporaryDirectory() as tmp:
        env_dir = Path(tmp) / "venv-di-prova"
        code, out = run([sys.executable, "-m", "venv", str(env_dir)], timeout=90)
    if code == 0:
        results.append(Result("ambiente virtuale", "OK", "python3 -m venv funziona"))
    else:
        hint = (
            "sudo apt install python3-venv python3-pip"
            if os_name in ("wsl", "linux")
            else "Reinstalla Python: brew reinstall python@3.12"
        )
        results.append(Result("ambiente virtuale", "KO", "python3 -m venv non funziona", [hint]))
    return results


def check_node() -> list[Result]:
    nvm_dir = os.environ.get("NVM_DIR") or str(Path.home() / ".nvm")
    nvm_scripts = [
        Path(nvm_dir, "nvm.sh"),
        Path("/opt/homebrew/opt/nvm/nvm.sh"),   # Homebrew su Mac Apple Silicon
        Path("/usr/local/opt/nvm/nvm.sh"),      # Homebrew su Mac Intel
    ]
    node_path = shutil.which("node") or ""
    managed = ("/.nvm/" in node_path or "/.asdf/" in node_path)
    has_nvm = managed or any(p.exists() for p in nvm_scripts)

    if not shutil.which("node"):
        hints = (["nvm install --lts"] if has_nvm
                 else ["Installa nvm con lo script della checklist, riapri il terminale, poi: nvm install --lts"])
        return [Result("node", "KO", "non trovato", hints)]

    _, out = run(["node", "--version"])
    version = out.lstrip("v")
    try:
        major = int(version.split(".")[0])
    except ValueError:
        major = 0

    results: list[Result] = []
    if major < NODE_MIN_MAJOR:
        results.append(Result("node", "KO", f"{version}, serve la {NODE_MIN_MAJOR} o superiore",
                              ["nvm install --lts && nvm alias default 'lts/*'"]))
    elif major % 2 == 1:
        results.append(Result("node", "!!", f"{version}, versione non LTS",
                              ["nvm install --lts && nvm alias default 'lts/*'"], required=False))
    else:
        results.append(Result("node", "OK", f"{version} (LTS)"))

    if shutil.which("npm"):
        _, npm_out = run(["npm", "--version"])
        results.append(Result("npm", "OK", first_version(npm_out)))
    else:
        results.append(Result("npm", "KO", "non trovato", ["Reinstalla Node con: nvm install --lts"]))

    if not has_nvm:
        results.append(Result("nvm", "!!", "non trovato",
                              ["Node funziona, ma nel corso usiamo nvm: vedi la checklist"], required=False))
    return results


def check_postgres(os_name: str, db_name: str) -> list[Result]:
    if not shutil.which("psql"):
        return [Result("postgresql", "KO", "psql non trovato", [
            install_hint(os_name, "brew install postgresql@16 && brew services start postgresql@16",
                         "sudo apt install postgresql"),
        ])]

    _, out = run(["psql", "--version"])
    results = [Result("postgresql", "OK", first_version(out))]

    code, out = run(["psql", "-w", "-d", db_name, "-tAc", "select 1"])
    if code == 0 and out.strip().endswith("1"):
        results.append(Result("connessione al database", "OK", f"database «{db_name}» raggiungibile"))
        return results

    low = out.lower()
    try:
        user = getpass.getuser()
    except Exception:
        user = "tuo-utente"
    if "role" in low and "does not exist" in low:
        hints = [f"Manca l'utente «{user}» in PostgreSQL"]
        hints.append(
            f"sudo -u postgres createuser --superuser {user}"
            if os_name in ("wsl", "linux")
            else f"createuser --superuser {user}"
        )
        detail = "utente PostgreSQL mancante"
    elif "database" in low and "does not exist" in low:
        hints = [f"createdb {db_name}"]
        detail = f"database «{db_name}» mancante"
    elif any(s in low for s in ("connection refused", "no such file", "could not connect", "is the server running")):
        hints = [
            "sudo service postgresql start"
            if os_name in ("wsl", "linux")
            else "brew services start postgresql@16"
        ]
        detail = "il server è spento"
    elif "no password supplied" in low:
        hints = ["Il server chiede una password: di solito succede se è impostata la variabile PGHOST",
                 "Prova: unset PGHOST, poi rilancia lo script. Se non basta, scrivi su Discord"]
        detail = "il server chiede una password"
    elif "password authentication failed" in low:
        hints = ["Password errata: controlla la checklist per la configurazione dell'utente"]
        detail = "password rifiutata"
    else:
        hints = ["Copia il messaggio qui sotto nel canale domande"]
        detail = out.splitlines()[0] if out else "errore sconosciuto"
    results.append(Result("connessione al database", "KO", detail, hints))
    return results


def check_gh(os_name: str) -> list[Result]:
    if not shutil.which("gh"):
        return [Result("github cli", "KO", "gh non trovato", [
            install_hint(os_name, "brew install gh", "Vedi la checklist: installazione di gh su Ubuntu"),
        ])]
    _, out = run(["gh", "--version"])
    results = [Result("github cli", "OK", first_version(out))]

    code, out = run(["gh", "auth", "status"])
    if code == 0:
        account = re.search(r"account (\S+)", out) or re.search(r"as (\S+)", out)
        who = account.group(1) if account else "accesso attivo"
        results.append(Result("accesso a github", "OK", who))
    else:
        results.append(Result("accesso a github", "KO", "non hai fatto il login", ["gh auth login"]))
    return results


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description="Verifica l'ambiente del corso.")
    parser.add_argument("--db", default="prova", help="database da usare per il test (default: prova)")
    args = parser.parse_args()

    os_name = detect_os()
    print(f"\n{BOLD}Corso intensivo di coding · verifica dell'ambiente{RESET}")
    print(f"{GREY}Sistema: {OS_LABEL[os_name]} · Python in uso: {sys.executable}{RESET}\n")

    if os_name == "windows":
        print(f"{RED}[KO]{RESET} {BOLD}sistema{RESET} · stai usando il terminale di Windows")
        print(f"     {GREY}→ Apri Ubuntu (WSL) e lancia lo script da lì{RESET}\n")
        return 1

    results: list[Result] = []
    results += check_git(os_name)
    results.append(check_vscode(os_name))
    results += check_python(os_name)
    results += check_node()
    results += check_postgres(os_name, args.db)
    results += check_gh(os_name)

    for result in results:
        result.print()

    required = [r for r in results if r.required]
    passed = sum(r.status == "OK" for r in required)
    warnings = sum(r.status == "!!" for r in results)
    print()
    if passed == len(required):
        print(f"{GREEN}{BOLD}Tutto pronto: {passed}/{len(required)} controlli superati.{RESET}")
        print("Fai uno screenshot e incollalo sulla tua riga del semaforo su Mural.")
    else:
        print(f"{RED}{BOLD}{passed}/{len(required)} controlli superati.{RESET}")
        print("Torna ai passi con [KO] nella checklist. Bloccato da 10 minuti, anche dopo l'AI? Casella rossa e messaggio su Discord.")
    if warnings:
        print(f"{YELLOW}{warnings} avvisi [!!]: non bloccano, ma sistemali quando puoi.{RESET}")
    print()
    return 0 if passed == len(required) else 1


if __name__ == "__main__":
    sys.exit(main())
