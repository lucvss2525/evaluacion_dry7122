import json

with open('dispositivos.json', 'r') as archivo:
    dispositivos_data = json.load(archivo)

for dispositivo in dispositivos_data["dispositivos"]:
    print(f"Nombre: {dispositivo['nombre']}")
    print(f"IP: {dispositivo['ip']}")
    print(f"Estado: {dispositivo['estado']}")
    print("-" * 30)
    