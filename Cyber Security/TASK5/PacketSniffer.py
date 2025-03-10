import scapy.all as scapy

def packet_sniffer():
    def process_packet(packet):
        if packet.haslayer(scapy.IP):
            print(f"Packet: {packet[scapy.IP].src} -> {packet[scapy.IP].dst}")

    scapy.sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    packet_sniffer()
