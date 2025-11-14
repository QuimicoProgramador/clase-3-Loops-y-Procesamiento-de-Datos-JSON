# ...existing code...
from typing import List, Dict

usuarios_azure: List[dict] = [
    {"nombre": "Carlos", "status_seguridad": "OK", "rol": "Admin"},
    {"nombre": "Ana", "status_seguridad": "PENDIENTE", "rol": "Desarrollador"},
    {"nombre": "Luis", "status_seguridad": "OK", "rol": "Admin"},
    {"nombre": "María", "status_seguridad": "PENDIENTE", "rol": "Admin"},
    {"nombre": "Jorge", "status_seguridad": "OK", "rol": "Soporte"},
]

def filtrar_pendientes(usuarios: List[dict]) -> List[dict]:
    """
    Devuelve una lista con los usuarios cuyo status_seguridad es 'PENDIENTE' (insensible a mayúsculas/minúsculas).
    """
    pendientes: List[dict] = []
    for usuario in usuarios:
        if usuario.get("status_seguridad", "").strip().upper() == "PENDIENTE":
            pendientes.append(usuario)
    return pendientes

if __name__ == "__main__":
    pendientes = filtrar_pendientes(usuarios_azure)
    print("Pendientes:", pendientes)
# ...existing code...