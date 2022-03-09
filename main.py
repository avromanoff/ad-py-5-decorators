# 1. Написать декоратор - логгер.
# Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
#
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
#
# 3. Применить написанный логгер к приложению из любого предыдущего д / з.

from log_tool import logger
from superheroes import hero_int

superheroes = ['Hulk', 'Captain America', 'Thanos']


# @logger(path='D:\\')
@logger(path='')  # пустой путь - лог в текущей директории
def most_intell(heroes_list):
    intell = 0
    hero_name = ''
    for superhero in heroes_list:
        if int(hero_int(superhero)) > int(intell):
            intell = hero_int(superhero)
            hero_name = superhero
    return hero_name


print(most_intell(superheroes))

