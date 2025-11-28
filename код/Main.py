from Ship import (
    Ship,
)
from Menu import (
    Menu,
)


ship_1 = Ship('radgsdf', 'gdagd', 'ghreh')
ship_2 = Ship()
menu = Menu()

is_running = True

def run() -> None:
    """Метод запуска работы."""

    is_running = True

    while (is_running):
        menu.print_main_menu()

        choice = int(input('Введите выбор: '))
        choice_ship = int(input('Введите порядковый номер корабля: '))
        ship = ship_1 if choice_ship == 1 else ship_2

        is_running = menu.main_menu(choice, ship)

run()
