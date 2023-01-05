# TODO здесь писать код

import random

class Buddhist:
    def __init__(self, karma=0) -> None:
        self.__karma  = karma

    def get_karma(self):
        return self.__karma 

    def set_karma(self, enlightenment_closer):
        self.__karma += enlightenment_closer

def one_day(count):
    if random.randint(1, 10):
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            misconduct  = random.choice(['KillerError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            karma_log.write(f'\nдень: {count} поступок - {misconduct}\n')
            return False
        
    else :
        return random.randint(1,7)

budhist = Buddhist()

day = 0

while budhist.get_karma() < 500:
    day += 1
    if one_day(day):
        pass

    else:
        budhist.set_karma(one_day(day))