import re

class Validador:
    @staticmethod
    def correo_valido(correo: str) -> bool:

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, correo))

    @staticmethod
    def telefono_valido(telefono: str) -> bool:
        patron = r'^\d{8}$'
        return bool(re.match(patron, telefono))
