class Ship:
    '''Класс для описания корабля'''

    def __init__(self, name = 'Нет названия', displacement = 1, type_ = 'Не определён'):
        '''Конструктор класса Ship

        Args:
            name: назваеие корабля,
            displacement: водоизмещение,
            type_: тип корабля.
        '''
        
        self.__name = name
        self.__displacement = displacement
        self.__type = type_

    def set_name(self, name) -> None:
        '''Сеттер названия корабля.

        Args:
            name: название корабля.
        '''

        self.__name = name
    
    def get_name(self) -> str:
        '''Геттер названия корабля.

        Returns:
            __name: название корабля.
        '''

        return self.__name
    
    def set_displacement(self, displacement) -> None:
        '''Сеттер водоизмещения корабля. Если задано значение < 0, то будет значение 1
        
        Agrs:
            displacement: водоизмещение корабля.
        '''

        self.__displacement = displacement

        if displacement <= 0:
            print('Вы ввели неверное значение')
            
            self.__displacement = 1
    
    def get_displacement(self) -> float:
        '''Геттер водоизмещения корабля.

        Returns:
            __displacement: водоизмещение корабля.
        '''

        return self.__displacement
    
    def set_type(self, type_) -> None:
        '''Сеттер типа корабля.

        Args:
            type_: тип корабля.
        '''

        self.__type = type_
    
    def get_type(self) -> str:
        '''Геттер типа корабля.

        Returns:
            __type: тип корабля.
        '''

        return self.__type
    
    def show_info(self) -> None:
        '''Вывод полной информации о корабле.'''

        print(f'Корабль: {self.__name}, Водоизмещение: {self.__displacement}, Тип: {self.__type}')

    def reset(self) -> None:
        '''Задаёт стандартные значения параметрам корабля.'''

        self.__name = 'Нет названия'
        self.__displacement = 1
        self.__type = 'Не определён'

    def is_military(self) -> bool:
        '''Проверяет, военный корабль или нет.

        Returns:
            bool: True - военный, False - нет.
        '''

        if self.__type.lower() in ['линкор', 'крейсер', 'авианосец', 'эсминец']:
            return True
        else: return False
