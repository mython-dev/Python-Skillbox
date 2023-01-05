# TODO здесь писать код


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()


class Air:

    def __str__(self) -> str:
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return  Storm()

        elif isinstance(other, Fire):
            return Vapor()

        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

class Fire:
    def __str__(self) -> str:
        return 'Огноь'

class Earth:
    def __str__(self) -> str:
        return 'Земля'
        


class  Storm():
    def __str__(self) -> str:
        return 'Шторм'


class Vapor():
    def __str__(self) -> str:
        return 'Пар'


class Dirt():
    def __str__(self) -> str:
        return 'Грязь'

water = Water()

air = Air()

fire = Fire()

earth = Earth()

print(air + water, water + fire, water + earth)
