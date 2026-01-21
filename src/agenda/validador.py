import re

class Validador:
    @staticmethod
    def correo_valido(correo: str) -> bool:

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, correo))

