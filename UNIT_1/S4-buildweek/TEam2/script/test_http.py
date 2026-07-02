import requests

# Indirizzo del Web Server nella DMZ
url = "http://172.16.10.10"

verbi_http = ["GET", "POST", "PUT", "DELETE"]

for verbo in verbi_http:
    try:
        risposta = requests.request(verbo, url, timeout=5)

        print("Verbo HTTP:", verbo)
        print("Codice risposta:", risposta.status_code)
        print("Risultato:", risposta.reason)
        print("-" * 30)

    except requests.exceptions.RequestException:
        print("Verbo HTTP:", verbo)
        print("Errore: il Web Server non è raggiungibile")
        print("-" * 30)