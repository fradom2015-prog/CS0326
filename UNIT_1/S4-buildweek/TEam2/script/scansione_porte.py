import socket

# Indirizzo del Web Server nella DMZ
host = "172.16.10.10"

# Porte principali da controllare
porte = [21, 22, 23, 25, 53, 80, 443, 8080]

print("Scansione porte sul dispositivo:", host)
print("-" * 40)

for porta in porte:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    risultato = sock.connect_ex((host, porta))

    if risultato == 0:
        print("Porta", porta, "APERTA")
    else:
        print("Porta", porta, "CHIUSA o non raggiungibile")

    sock.close()

print("-" * 40)
print("Scansione completata")