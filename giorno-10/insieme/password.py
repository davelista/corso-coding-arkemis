"""LE PASSWORD · lo scriviamo insieme, dal vivo.

Si prova con:  python3 password.py
"""

import hashlib
import secrets
from pwdlib import PasswordHash

def hash_password(password: str) -> str:
    psw_byte = password.encode() # Trasformo la psw in byte
    hash_psw_obj = hashlib.sha256(psw_byte) # Trasformo i byte in un oggetto 
    hash_psw_str = hash_psw_obj.hexdigest() # Codifica esadecimale dell'oggetto
    return hash_psw_str

# Aggiunta del sale
def calcolo_hash_password(password: str) -> str:
    salt = secrets.token_hex() # Token esadecimale di lunghezza 8
    psw_impronta = hash_password(password + salt)
    return f"{salt}${psw_impronta}"

# Controllo per il login
def cnotrollo_password(password_inserita: str, password_salvata: str) -> bool:
    salt, password_hash = password_salvata.split("$")
    ricalcolo = hash_password((salt + password_inserita))
    return password_hash == ricalcolo

# Con la libreria tutto questo diventa:
algoritmo = PasswordHash.recommended() # Mi restituisce l'algoritmo raccomandato
def calcolo_hash_password_lib(password: str) -> str:
    password_hash = algoritmo.hash(password)
    return password_hash

def controllo_password_lib(password_inserita: str, password_salvata: str) -> bool:
    check = algoritmo.verify(password_inserita, password_salvata) #Restituisce True o False
    return check