# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *
from randomwin import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            print("Хотите попытать удачу и убежать от соперника?? (Введите: Хачу)")
            answer = input('Ответ:')
            if answer == "Хачу":
                print("Твой вероятность пройти уровень зависить от твой опыта и составляет:", hero._experience / 2, "%")
                exp = hero._experience
                if Random(hero).check(exp):
                    while dragon.is_alive():
                        hero.attack(dragon)
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** от вас откусили кусочек... **')
                    print('Ваш накопленный опыт:', hero._experience)
            else:
                if dragon.check_answer(answer):
                    hero.attack(dragon)
                    print('Верно! \n** дракон кричит от боли **')
                    print('Ваш накопленный опыт:', hero._experience)
                else:
                    dragon.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
                    print('Ваш накопленный опыт:', hero._experience)
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')
        hero._experience+=10

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def game_trollnament(hero, troll_list):
    for troll in troll_list:
        print('Вышел', troll._color, 'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            print("Хотите попытать удачу и убежать от соперника?? (Введите: Хачу)")
            answer = input('Ответ:')
            if answer == "Хачу":
                print("Твой вероятность пройти уровень зависить от твой опыта и составляет:", hero._experience/2, "%")
                exp = hero._experience
                if Random(hero).check(exp):
                    while troll.is_alive():
                        hero.attack(troll)
                else:
                    troll.attack(hero)
                    print('Ошибка! \n** от вас откусили кусочек... **')
                    print('Ваш накопленный опыт:', hero._experience)
            else:
                if troll.check_answer(answer):
                    hero.attack(troll)
                    print('Верно! \n** троллю неприятно **')
                    print('Ваш накопленный опыт:', hero._experience)
                else:
                    troll.attack(hero)
                    print('Ошибка! \n** от вас откусили кусочек... **')
                    print('Ваш накопленный опыт:', hero._experience)
        if troll.is_alive():
            break
        print('Тролль', troll._color, 'затроллен!\n')
        hero._experience+=20

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вас сожрали...')

def rod_dragon(number):
    if number%100 in [11,12,13,14]:return 'драконов'
    if number%10 in [2,3,4]:return 'дракона'
    if number%10==1:return 'дракон'
    else:return 'драконов'

def rod_troll(number):
    if number%100 in [11,12,13,14]:return 'троллей'
    if number%10 in [2,3,4]:return 'тролля'
    if number%10==1:return 'тролль'
    else:return 'троллей'

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        word = input()
        hero = Hero(word)
        if randint(1,2)==1:
            dragon_number = randint(2,15)
            dragon_list = generate_dragon_list(dragon_number)
            print('У Вас на пути', dragon_number, rod_dragon(dragon_number)+'!')
            game_tournament(hero, dragon_list)
        else:
            troll_number = randint(2,15)
            troll_list = generate_troll_list(troll_number)
            print('Вам не дают пройти', troll_number, rod_troll(troll_number)+'!')
            game_trollnament(hero, troll_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')