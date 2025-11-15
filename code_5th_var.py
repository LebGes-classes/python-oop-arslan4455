class Ship:
    def __init__(self, name = 'Нет названия', displacement = 1, type_ = 'Не определён'):
        self.__name = name
        self.__displacement = displacement
        self.__type = type_

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_displacement(self, displacement):
        self.__displacement = displacement
        if displacement <= 0:
            print('Вы ввели неверное значение')
            self.__displacement = 1
    
    def get_displacement(self):
        return self.__displacement
    
    def set_type(self, type_):
        self.__type = type_
    
    def get_type(self):
        return self.__type
    
    def show_info(self):
        print(f'Корабль: {self.__name}, Водоизмещение: {self.__displacement}, Тип: {self.__type}')

    def reset(self):
        self.__name = 'Нет названия'
        self.__displacement = 1
        self.__type = 'Не определён'

    def is_military(self):
        if self.__type.lower() in ['линкор', 'крейсер', 'авианосец', 'эсминец']:
            return True
        else: return False

class Menu:
    def __init__(self, ship: Ship):
        self.ship = ship

    def show_menu(self):
        print('МЕНЮ')
        print('1. Показать информацию')
        print('2. Изменить название')
        print('3. Изменить водоизмещение')
        print('4. Изменить тип корабля')
        print('5. Корабль военный?')
        print('6. Сбросить')
        print('EXIT - выход')
    
    def run(self):
        while True:
            self.show_menu()
            choice = input('Выберите действие: ')

            match choice:
                case '1':
                    self.ship.show_info()
                case '2':
                    new_name = input('Введите название: ')
                    self.ship.set_name(new_name)
                case '3':
                    new_displacement = float(input('Введите водоизмещение (>0): '))
                    if new_displacement <= 0:
                        print('Вы ввели неверное значение')
                        new_displacement = 1
                    self.ship.set_displacement(new_displacement)
                case '4':
                    new_type = input('Введите новый тип: ')
                    self.ship.set_type(new_type)
                case '5':
                    if self.ship.is_military():
                        print('Да')
                    else:
                        print('Нет')
                case '6':
                    self.ship.reset()
                case 'EXIT':
                    break
                    
class Main():
    
    ship1 = Ship()
    ship2 = Ship()

    print('Создано 2 корабля')

    ship1.show_info()
    ship2.show_info()

    ship_choice = input('Выберите корабль (1 или 2): ')

    if ship_choice == '1':
        menu = Menu(ship1)
    elif ship_choice == '2':
        menu = Menu(ship2)
    else:
        raise ValueError
    
    menu.run()
