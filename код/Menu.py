from Ship import (
    Ship,
)


class Menu:
    '''Класс меню для работы пользовательского меню.'''

    def print_main_menu(self) -> None:
        '''Вывод пунктов главного пользовательского меню.'''

        print(
            '\n1: Печать информации о корабле.\n'
            '2: Изменить название корабля.\n'
            '3: Изменить водоизмещение корабля.\n'
            '4: Изменить тип корабля.\n'
            '5: Корабль военный?\n'
            '6: Получить информацию о названии корабля.\n'
            '7: Получить информацию о водоизмещении корабля.\n'
            '8: Получить информацию о типе корабля.\n'
            '9: Сброс значений.\n'
            '0: ВЫХОД ИЗ ПРОГРАММЫ!\n'
        )


    def main_menu(self, choice: int, ship: Ship) -> None:
        '''Метод, выполняющий средства пользовательского меню.
        
        Args:
            choice: выбор пользоввателя.

        Returns:
            is_running: Продолжается ли работа программы.
        '''

        is_running = True

        match choice:
            case 0:
                is_running = False
            case 1:
                ship.show_info()
            case 2:
                name = input('Введите название корабля: ')

                ship.set_name(name)
            case 3:
                displacement = input('Введите водоизмещение корабля (>0): ')

                ship.set_displacement(displacement)
            case 4:
                type_ = input('Введите тип корабля: ')

                ship.set_type(type_)
            case 5:
                is_mil = ship.is_military()
                print('Да' if is_mil else 'Нет')
            case 6:
                print(ship.get_name())
            case 7:
                print(ship.get_displacement())
            case 8:
                print(ship.get_type())
            case 9:
                ship.reset()

        return is_running
