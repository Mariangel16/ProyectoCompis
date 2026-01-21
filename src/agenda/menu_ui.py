from .agenda import Agenda
from .contacto import Contacto

class MenuUI:
    def __init__(self, agenda: Agenda):
        self.agenda = agenda

    def _leer_no_vacio(self, msg: str) -> str:
        while True:
            s = input(msg).strip()
            if s:
                return s
            print("Entrada vacía. Intenta de nuevo.")

    def mostrar_menu(self) -> None:
        print("\n=== AGENDA ===")
        print("1) Agregar contacto")
        print("2) Listar contactos")
        print("3) Buscar contacto")
        print("0) Salir")

    def ejecutar(self) -> None:
        while True:
            self.mostrar_menu()
            op = input("Opción: ").strip()

            if op == "1":
                nombre = self._leer_no_vacio("Nombre: ")
                correo = self._leer_no_vacio("Correo: ")
                telefono = self._leer_no_vacio("Teléfono: ")
                self.agenda.agregar_contacto(Contacto(nombre, correo, telefono))
                print("Contacto agregado.")

            elif op == "2":
                contactos = self.agenda.listar_contactos()
                if not contactos:
                    print("No hay contactos.")
                else:
                    for i, c in enumerate(contactos, start=1):
                        print(f"{i}. {c.nombre} | {c.correo} | {c.telefono}")

            elif op == "3":
                criterio = self._leer_no_vacio("Buscar (nombre/correo/teléfono): ")
                c = self.agenda.buscar_contacto(criterio)
                if c is None:
                    print("No encontrado.")
                else:
                    print(f"Encontrado: {c.nombre} | {c.correo} | {c.telefono}")

            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
