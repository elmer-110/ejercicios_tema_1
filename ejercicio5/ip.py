import sys

def descomponer_ip(ip):
    octetos = ip.split('.')
    if len(octetos) != 4 or not all(o.isdigit() and 0 <= int(o) <= 255 for o in octetos):
        print("Error: Dirección IP inválida.")
        
        return
    for i, octeto in enumerate(octetos, start=1):
        print(f"Octeto {i}: {octeto}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python descomponer_ip.py <direccion_ip>")
    else:
        descomponer_ip(sys.argv[1])
