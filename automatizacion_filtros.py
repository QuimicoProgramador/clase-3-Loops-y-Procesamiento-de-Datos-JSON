# ...existing code...
from typing import List, Dict

usuarios_azure: List[dict] = [
    {"nombre": "Carlos", "status_seguridad": "OK", "rol": "Admin"},
    {"nombre": "Ana", "status_seguridad": "PENDIENTE", "rol": "Desarrollador"},
    {"nombre": "Luis", "status_seguridad": "OK", "rol": "Admin"}
]
# ...existing code...

def filtrar_usuarios(usuarios: List[dict]) -> Dict[str, List[dict]]:
    """
    Devuelve un diccionario con dos listas:
    - 'admins': usuarios cuyo rol es 'Admin' (insensible a mayúsculas).
    - 'pendientes': usuarios cuyo status_seguridad es 'PENDIENTE' (insensible a mayúsculas).
    Un mismo usuario puede aparecer en ambas listas si cumple ambas condiciones.
    """
    admins: List[dict] = []
    pendientes: List[dict] = []

    for usuario in usuarios:
        rol = usuario.get("rol", "").strip().lower()
        status = usuario.get("status_seguridad", "").strip().upper()

        if rol == "admin":
            admins.append(usuario)
        if status == "PENDIENTE":
            pendientes.append(usuario)

    return {"admins": admins, "pendientes": pendientes}

if __name__ == "__main__":
    resultado = filtrar_usuarios(usuarios_azure)
    print("Admins:", resultado["admins"])
    print("Pendientes:", resultado["pendientes"])
# ...existing code...