from agenda.agenda import Agenda
from agenda.menu_ui import MenuUI
from agenda.validador import Validador

def main() -> None:
    agenda = Agenda()
    menu = MenuUI(agenda)
    menu.ejecutar()

if __name__ == "__main__":
    main()
