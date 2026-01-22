from .agenda import Agenda
from .contacto import Contacto
from .validador import Validador 

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
                print(">> Ingresando nuevo contacto:")
                nombre = self._leer_no_vacio("Nombre: ") #validar que no este vacio

                # 2. Correo, se valida hasta que sea correcto el correo. 
                while True:
                    correo = input("Correo: ").strip()
                    if Validador.correo_valido(correo):
                        break 
                    print("Error: Correo inválido (ej. usuario@dominio.com).")

                # 3. Teléfono realiza el mismo proceso que correo; El telefono tiene que ser de 8 numeros
                while True:
                    telefono = input("Teléfono: ").strip()
                    if Validador.telefono_valido(telefono):
                        break 
                    print("Error: Teléfono inválido (deben ser 8 dígitos).")

                nuevo_contacto=Contacto(nombre,correo,telefono)
                self.agenda.agregar_contacto(nuevo_contacto)
                print("Contacto agregado exitosamente.")

            elif op == "2":
                contactos = self.agenda.listar_contactos()
                if not contactos:
                    print("No hay contactos.")
                else:
                    for i, c in enumerate(contactos, start=1):
                        print(f"{i}. {c.nombre} | {c.correo} | {c.telefono}")

            elif op == "3":
                criterio = self._leer_no_vacio("Buscar (nombre/correo/teléfono): ")
                resultados = self.agenda.buscar_contactos(criterio)

                if not resultados:
                    print("No encontrado.")
                else:
                    print("Resultados:")
                    for i, c in enumerate(resultados, start=1):
                        print(f"{i}. {c.nombre} | {c.correo} | {c.telefono}")

            elif op == "0":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
