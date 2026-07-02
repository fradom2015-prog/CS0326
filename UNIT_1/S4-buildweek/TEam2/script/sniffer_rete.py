#!/usr/bin/env python3
"""
Sniffer di rete - Progetto Compagnia Theta
Eseguire con: sudo python3 sniffer_rete.py
"""

import socket
import struct

# Apertura raw socket (richiede sudo)
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

print("Sniffer avviato. Premi Ctrl+C per fermare.\n")
print(f"{'Protocollo':<10} {'Sorgente':<18} {'Destinazione'}")
print("-" * 50)

PROTOCOLLI = {1: "ICMP", 6: "TCP", 17: "UDP"}

try:
    while True:
        raw, _ = sock.recvfrom(65535)
        ip = raw[14:34]  # intestazione IP (salta 14 byte Ethernet)
        proto = ip[9]
        src = socket.inet_ntoa(ip[12:16])
        dst = socket.inet_ntoa(ip[16:20])
        nome = PROTOCOLLI.get(proto, f"PROTO-{proto}")
        print(f"{nome:<10} {src:<18} {dst}")
except KeyboardInterrupt:
    print("\nSniffer fermato.")
finally:
    sock.close()
