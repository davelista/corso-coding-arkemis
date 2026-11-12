"""Verifica la vostra risposta. Questo file NON si tocca.

python verifica.py "il luogo"
"""

import base64
import hashlib
import sys
import unicodedata

_GIUSTO = "8a2fa80541b8ed1bd62c"
_MESSAGGIO = "RVNBVFRPLiBMJ0FuZWxsbyDDqCBuZWwgR2lhcmRpbm8sIHNlcG9sdG8gc290dG8gaWwgdmVjY2hpbyBmYWdnaW8uCgpMYSBjb25mZXNzaW9uZSBkaSBCaWxibzoKwqtWb2xldm8gc29sbyB2ZWRlcmxvIHVuJ3VsdGltYSB2b2x0YS4gUG9pIG5vbiByaXVzY2l2byBwacO5IGEgcmlkYXJsbyBpbmRpZXRybywKZSBhbGxvcmEgbCdobyBuYXNjb3N0byBkb3ZlIG5lc3N1bm8gc2NhdmEgbWFpLiBEaWNpb3R0byBtaW51dGksIGNvbiBsZSBtYW5pLgpNaSBkaXNwaWFjZSwgRnJvZG8uIMOIIHBpw7kgZm9ydGUgZGkgbWU6IMOoIHBpw7kgZm9ydGUgZGkgdHV0dGkuwrsKClNjcml2ZXRlIGlsIGx1b2dvIGluIHNxdWFkcmEubWQsIHBvaSBjb21taXQgZSBwdXNoOiAiQ2FzbyBjaGl1c28iLgpQb2kgYWl1dGF0ZSB1bidhbHRyYSBzcXVhZHJhLCBzb2xvIGEgdm9jZS4="
_INDIZI = {
    "8f3358164d8e23da10d4": "U0JBR0xJQVRPLiBSaWxlZ2dldGUgbGEgdGVzdGltb25pYW56YSBkaSBFbHJvbmQu",
    "24a107d9213313430902": "U0JBR0xJQVRPLiBTdWwgcG9udGUgcXVhbGN1bm8gY2kgw6ggcGFzc2F0bywgZSBiYXN0YTogcXVhbnRvIHNpIMOoIGZlcm1hdG8/",
    "25347bb43079198f9e29": "U0JBR0xJQVRPLiBMw6wgbCdBbmVsbG8gw6ggc3RhdG8gcHJlc28sIG5vbiBuYXNjb3N0by4=",
    "b2d7a079ea179b2ea3b1": "U0JBR0xJQVRPLiBHdWFyZGF0ZSBsJ29yYTogaW4gcXVlbGxhIHN0YW56YSBjaSDDqCBzdGF0byBwcmltYSBvIGRvcG8gaWwgZnVydG8/",
    "a23016ff21bbed29d9a8": "U0JBR0xJQVRPLiBJbiBjdWNpbmEgYydlcmEgU2FtLCBlIFNhbSBub24gcGVyZGUgZCdvY2NoaW8gbmllbnRlIGNoZSBzaSBtYW5naS4=",
}
_PAROLE_INUTILI = {"il", "lo", "la", "l", "nel", "nella", "nello", "in", "al", "alla", "sotto", "dentro"}


def _normalizza(testo):
    testo = unicodedata.normalize("NFKD", testo.lower()).encode("ascii", "ignore").decode()
    parole = testo.replace("'", " ").replace('"', " ").split()
    while parole and parole[0] in _PAROLE_INUTILI:
        parole = parole[1:]
    return " ".join(parole)


def _impronta(testo):
    return hashlib.sha256(("gran-burrone:" + testo).encode()).hexdigest()[:20]


def verifica(luogo):
    impronta = _impronta(_normalizza(luogo))
    if impronta == _GIUSTO:
        return base64.b64decode(_MESSAGGIO).decode()
    if impronta in _INDIZI:
        return base64.b64decode(_INDIZI[impronta]).decode()
    return "SBAGLIATO. Tornate agli indizi: quale tappa non avete ancora usato?"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Uso: python verifica.py "il luogo"', file=sys.stderr)
        sys.exit(1)
    print(verifica(" ".join(sys.argv[1:])))
