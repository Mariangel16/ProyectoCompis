
# Fase 0

from dataclasses import dataclass
from typing import Optional, List

# Clase Contacto

@dataclass
class Contacto:
    nombre: str
    correo: str
    telefono: str


# Clase Validador

class Validador:

    @staticmethod
    def correo_valido(correo: str) -> bool:
        pass  # se implementa en otra fase

    @staticmethod
    def telefono_valido(telefono: str) -> bool:
        pass  # se implementa en otra fase


# Clase Agenda

class Agenda:

    def __init__(self):
        self._estructura = None  # aquí irá la estructura de datos elegida

    def agregar_contacto(self, contacto: Contacto) -> bool:
        pass

    def buscar_contacto(self, criterio: str) -> Optional[Contacto]:
        pass

    def editar_contacto(self, criterio: str, nuevo: Contacto) -> bool:
        pass

    def eliminar_contacto(self, criterio: str) -> bool:
        pass

    def listar_contactos(self) -> List[Contacto]:
        pass


# Clase Menu / Interfaz

class MenuUI:

    def __init__(self, agenda: Agenda):
        self.agenda = agenda

    def mostrar_menu(self):
        pass

    def ejecutar(self):
        pass

# Punto de entrada

def main():
    agenda = Agenda()
    menu = MenuUI(agenda)
    menu.ejecutar()


if __name__ == "__main__":
    main()
