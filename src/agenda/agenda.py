from typing import List, Optional
from .contacto import Contacto

class Agenda:
    def __init__(self):
        self._contactos: List[Contacto] = []  # base temporal (luego cambian por su estructura)

    def agregar_contacto(self, contacto: Contacto) -> bool:
        self._contactos.append(contacto)
        return True

    def buscar_contacto(self, criterio: str) -> Optional[Contacto]:
        criterio = criterio.strip().lower()
        for c in self._contactos:
            if c.nombre.lower() == criterio or c.correo.lower() == criterio or c.telefono == criterio:
                return c
        return None

    def listar_contactos(self) -> List[Contacto]:
        return list(self._contactos)
