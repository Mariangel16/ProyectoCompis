from typing import List, Optional
from .contacto import Contacto

class Agenda:
    def __init__(self):
        self._contactos: List[Contacto] = [] 

    def agregar_contacto(self, contacto: Contacto) -> bool:
        self._contactos.append(contacto)
        return True

    def buscar_contactos(self, criterio: str) -> List[Contacto]:
        criterio = criterio.strip().lower()
        resultados: List[Contacto] = []

        for c in self._contactos:
            if (criterio in c.nombre.lower()
                or criterio in c.correo.lower()
                or criterio in c.telefono):
                resultados.append(c)

        return resultados

    def listar_contactos(self) -> List[Contacto]:
        return list(self._contactos)
