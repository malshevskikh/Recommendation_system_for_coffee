import csv
from operator import itemgetter, attrgetter, methodcaller
from geopy.distance import geodesic as GD
import tree_st
import re
import lab3, lab4
from lab3 import coffe_set, countries, tree


def labs_together(coffe_set, countries, tree):
    print("---------------------------------------------------------------------------------------------")
    print("Что вы предпочитаете сделать в первую очередь?")
    print("1. Отфильтровать список кофе")
    print("2. Сгенерировать рекомендации на основе списка кофе")
    print("3. Закончить")

    i = False
    main_arr = []

    while i == False:
        u = input("Выберите пункт от 1 до 3: ")
        if u.isdigit() == True:
            u = int(u)
            if (u != 1 and u != 2 and u != 3):
                print('Такого номера нет')
                i = True
            elif (u == 1):
                filters = lab4.menu_filter_choose(coffe_set)
                main_arr = lab4.starting_search(filters, coffe_set)
                i = True
            elif (u == 2):
                main_arr = lab3.menu(coffe_set, countries, tree)
                i = True
            elif (u == 3):
                i = True
        else:
            print('Такого номера нет')
            i = False

    for i in main_arr:
        print(i)

    z = False

    while z == False:
        print("Выберите следющий пункт")
        print("1. Отфильтровать список кофе")
        print("2. Сгенерировать рекомендации на основе списка кофе")
        print("3. Отобразить текущий сфорированный список")
        print("4. Сбросить текущий список до исходного")
        print("5. Закончить преобразования со списком")

        x = False
        while x == False:
            u = input("Выберите пункт от 1 до 5: ")
            if u.isdigit() == True:
                u = int(u)
                if (u != 1 and u != 2 and u != 3 and u != 4 and u != 5):
                    print('Такого номера нет')
                    x = True
                    z = False
                elif (u == 1):
                    filters = lab4.menu_filter_choose(main_arr)
                    main_arr = lab4.starting_search(filters, main_arr)
                    x = True
                    z = False
                elif (u == 2):
                    main_arr = lab3.menu(main_arr, countries, tree)
                    x = True
                    z = False
                elif (u == 3):
                    d = len(main_arr)
                    r = 1
                    for i in range(0, d):
                        print("Кофе №", r, "-", main_arr[i][0])
                        r = r + 1
                    x = True
                    z = False
                elif (u == 4):
                    main_arr = coffe_set
                    x = True
                    z = False
                elif (u == 5):
                    x = True
                    z = True
            else:
                print('Такого номера нет')
                x = False
                z = False



def menu_for_rk(coffe_set, countries, tree):
    v = False
    while v == False:
        print("Выберите пункт:")
        print("1. Лабораторная №3")
        print("2. Лабораторная №4")
        print("3. РК №1")
        print("4. Закончить")
        i = False
        while i == False:
            u = input("Выберите пункт от 1 до 4: ")
            if u.isdigit() == True:
                u = int(u)
                if (u != 1 and u != 2 and u != 3 and u != 4):
                    print('Такого номера нет')
                    i = True
                elif (u == 1):
                    lab3.menu(coffe_set, countries, tree)
                    i = True
                elif (u == 2):
                    filters = lab4.menu_filter_choose(coffe_set)
                    lab4.starting_search(filters, coffe_set)
                    i = True
                elif (u == 3):
                    labs_together(coffe_set, countries, tree)
                    i = True
                elif (u == 4):
                    i = True
                    v = True
            else:
                print('Такого номера нет')
                i = False


menu_for_rk(coffe_set, countries, tree)