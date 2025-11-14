proyecto_detalles: dict = {"nombre": "DeFi Tracker", "estado": "En curso", "prioridad": 95}

print("\nDetalles del Proyecto:")
for clave, valor in proyecto_detalles.items(): # .items() es clave aquí
    print(f"{clave.upper()} del proyecto es: {valor}")