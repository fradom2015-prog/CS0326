import socket
import os
import sys
import ipaddress
import time

def valida_ip(ip_str):
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False

def valida_porta(porta):
    return 1 <= porta <= 65535

def main():
    # 1. Input dell'IP target (con validazione)
    target_ip = input("Inserisci l'IP della macchina target: ").strip()
    if not valida_ip(target_ip):
        print("Errore: IP non valido.")
        sys.exit(1)

    # 2. Input della porta target (con validazione)
    try:
        target_port = int(input("Inserisci la porta UDP della macchina target: ").strip())
        if not valida_porta(target_port):
            raise ValueError
    except ValueError:
        print("Errore: porta non valida (deve essere tra 1 e 65535).")
        sys.exit(1)

    # 4. Numero di pacchetti da inviare
    try:
        num_packets = int(input("Quanti pacchetti da 1 KB vuoi inviare? ").strip())
        if num_packets <= 0:
            raise ValueError
    except ValueError:
        print("Errore: numero di pacchetti non valido.")
        sys.exit(1)

    # 3. Costruzione del pacchetto: 1 KB di dati casuali
    packet_size = 1024
    payload = os.urandom(packet_size)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print(f"\nInvio di {num_packets} pacchetti da {packet_size} byte a {target_ip}:{target_port}...\n")

    sent = 0
    errors = 0
    start_time = time.time()

    try:
        for i in range(num_packets):
            try:
                sock.sendto(payload, (target_ip, target_port))
                sent += 1
            except socket.error as e:
                errors += 1
                print(f"Errore invio pacchetto {i+1}: {e}")
    except KeyboardInterrupt:
        print("\nInterrotto dall'utente.")
    finally:
        sock.close()
        elapsed = time.time() - start_time
        total_kb = sent * packet_size / 1024
        speed = total_kb / elapsed if elapsed > 0 else 0

        print("\n--- Statistiche ---")
        print(f"Pacchetti inviati con successo: {sent}")
        print(f"Errori: {errors}")
        print(f"Tempo impiegato: {elapsed:.2f} s")
        print(f"Dati totali inviati: {total_kb:.2f} KB")
        print(f"Velocità media: {speed:.2f} KB/s")

if __name__ == "__main__":
    main()
