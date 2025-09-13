from scapy.all import *

# Realizar un escaneo de puertos (simulación de reconocimiento)
def escanear_puertos(ip):
    for puerto in range(1, 1020):
        respuesta = sr1(IP(dst=ip)/TCP(dport=puerto, flags="S"), timeout=0.1, verbose=0)
        if respuesta:
            if respuesta.haslayer(TCP) and respuesta[TCP].flags == 18:
                print(f"Puerto {puerto} abierto en {ip}")

# Ejecutar el escaneo de puertos
ip_objetivo = "192.168.1.1"
escanear_puertos(ip_objetivo)
