import csv
from operator import itemgetter, attrgetter, methodcaller
from geopy.distance import geodesic as GD
import tree_st
import re


def unique_list(l):
    u = []
    for i in l:
        if i not in u:
            u.append(i)
    return u

def compare_five_lists(l):
    result = []
    vr = []
    h = len(l)

    for i in l:
        for j in i:
            vr.append(j)

    d = len(vr)
    if d != 1:
        for i in range(0, d):
            c = 1
            #print("i", i)
            if i != vr[d-1]:
                for j in range(i+1, d):
                    #print("j", j)
                    if vr[i] == vr[j]:
                        c = c + 1
                if c == len(l):
                    result.append(vr[i])
    elif d == 1:
        result.append(vr[0])
    print("Список с подробными данными:")
    d = len(result)
    r = 1
    for i in range(0, d):
        print("Кофе №", r, "-", result[i])
        r = r + 1

    return result

def menu_filter_choose(coffe_list):
    print("ПОИСК ПО ФИЛЬТРУ")
    d = len(coffe_list)
    r = 1
    for i in range(0, d):
        print("Кофе №", r, "-", coffe_list[i][0])
        r = r + 1
    print("Выберите 1 или несколько фильтров из перечисленных и введите их через пробел: вкус, граммовка, обжарка, страна, сорт")
    q = False
    some_filters = []
    s = []
    while q == False:
        some_filters = input("Фильтры: ")
        some_filters = re.split(' |, |; ', some_filters)
        for i in some_filters:
            if (i != 'вкус' and i != 'граммовка' and i != 'обжарка' and i != 'страна' and i != 'сорт'):
                print(i, "- такого фильтра нет")
                q = False
                break
            else:
                q = True
    #print(some_filters)
    new_some_filters = unique_list(some_filters)
    if (some_filters != new_some_filters):
         print("Вы добавили несколько потворяющихся фильтров, поэтому повторения были устранены")
    some_filters = new_some_filters
    return some_filters

def delice_filter(cof_list, delices):
    delice_filter_list = []
    for i in cof_list:
        tastes = i[1]
        z = i[1].find(",")
        if z == -1:
            if i[1] in delices:
                delice_filter_list.append(i)
        else:
            p = False
            t = i[1].split(', ')
            tastes = re.split(' |, ', i[1])
            #print(tastes, "_____", t)
            for j in tastes:
                if j in delices:
                    p = True
            if p == True:
                delice_filter_list.append(i)
    if delice_filter_list == []:
        print("По вашему запросу ничего не найдено! Возможно вы неправильно ввели данные")
    return delice_filter_list

def weight_filter(cof_list, gramm1, gramm2):
    print("Сортировка по граммовке")
    i = False
    weight_filter_list = []
    cof_list = cof_list[1:]
    if gramm1 == gramm2 == None:
        print("Вы не ввели границы диапазона!")
    else:
        for i in cof_list:
            if gramm1 == None or gramm2 == None:
                if gramm1 == None:
                    if int(i[2]) <= gramm2:
                        weight_filter_list.append(i)
                elif gramm2 == None:
                    if gramm1 <= int(i[2]):
                        weight_filter_list.append(i)
            elif (gramm1 <= int(i[2]) <= gramm2):
                weight_filter_list.append(i)

    #print("нет ограничений!!!!:::", weight_filter_list)
    if  weight_filter_list == []:
        print("По вашему запросу ничего не найдено! Возможно вы неправильно ввели данные")

    return weight_filter_list

def obg_filter(cof_list, obg):
    print("Сортировка по обажрке")
    print(obg)
    obg_filter_list = []
    '''
    for i in obg:
        if i != 'светлая' and i != 'средняя' and i != 'темная':
            print(i, "- такой обжарки нет")
            s = False
            break
        else:
            s = True
    '''

    new_obg= unique_list(obg)
    if (new_obg != obg):
        print("Вы добавили несколько потворяющихся обжарок, поэтому повторения были устранены")
        obg = new_obg
    #print(obg)
    for i in cof_list:
        if i[3] in obg:
            obg_filter_list.append(i)

    #print(obg_filter_list)
    if obg_filter_list == []:
        print("По вашему запросу ничего не найдено! Возможно вы неправильно ввели данные")
    return obg_filter_list

def country_filter(cof_list, countries):
    print("Сортировка по странам")

    countries_filter_list = []

    new_countries = unique_list(countries)
    if (new_countries != countries):
        print("Вы добавили несколько потворяющихся стран, поэтому повторения были устранены")
        countries = new_countries

    for i in cof_list:
        if i[4] in countries:
            countries_filter_list.append(i)

    if countries_filter_list == []:
        print("По вашему запросу ничего не найдено! Возможно вы неправильно ввели данные")

    return countries_filter_list

def sort_filter(cof_list, sort):
    print("Сортировка по сорту кофе")
    print("Выберите сорт зерен (арабика или робуста), которые хотите учесть в кофе и перечислите через запятые:")
    i = False
    sort_filter_list = []
    for i in sort:
        if i != 'арабика' and i != 'робуста':
            print(i, "- такого сорта нет")

    new_sort = unique_list(sort)
    if (new_sort != sort):
        print("Вы добавили несколько потворяющихся сортов, поэтому повторения были устранены")
    sort = new_sort
    #print(sort)
    for i in cof_list:
        if i[5] in sort:
            sort_filter_list.append(i)

    #print(sort_filter_list)
    if sort_filter_list == []:
        print("По вашему запросу ничего не найдено! Возможно вы неправильно ввели данные")
    #for i in sort_filter_list:
    #    print(i)
    return sort_filter_list


def starting_search(some_filters, cof_list):
    #print(some_filters)
    check_arr = []
    delice_filter_list = []
    weight_filter_list = []
    obg_filter_list = []
    countries_filter_list = []
    sort_filter_list = []
    for i in some_filters:
        if i == 'вкус':
            #print("вкус тут")
            delice_filter_list = delice_filter(cof_list)
            check_arr.append(delice_filter_list)
        elif i == 'граммовка':
            #print("граммовка тут")
            weight_filter_list = weight_filter(cof_list)
            #for i in weight_filter_list:
            #   print(i)
            check_arr.append(weight_filter_list)
        elif i == 'обжарка':
            #print("обжарка тут")
            obg_filter_list = obg_filter(cof_list)
            check_arr.append(obg_filter_list)
        elif i == 'страна':
            #print("страна тут")
            countries_filter_list = country_filter(cof_list)
            check_arr.append(countries_filter_list)
        elif i == 'сорт':
            #print("сорт тут")
            sort_filter_list = sort_filter(cof_list)
            check_arr.append(sort_filter_list)

    #check_arr.append(delice_filter_list)
    #check_arr.append(weight_filter_list)
    #check_arr.append(obg_filter_list)
    #check_arr.append(countries_filter_list)
    #check_arr.append(sort_filter_list)
    main_filter_list = []

    main_filter_list = compare_five_lists(check_arr)
    print("С учетом всех фильтров, вот список кофе:")

    d = len(main_filter_list)
    r = 1
    for i in range(0, d):
        print("Кофе №", r, "-", main_filter_list[i][0])
        r = r + 1

    print("1. Заново отфильтровать исходный список?")
    print("2. Отфильтровать сформированный список?")
    print("3. Закончить")
    b = False
    while (b == False):
        u = input("Выберите цифру от 1 до 3: ")
        if u.isdigit() == True:
            u = int(u)
            if (u != 1 and u != 2 and u != 3):
                print('Такого номера нет')
                b = False
            elif (u == 1):
                b = True
                filters = menu_filter_choose(coffe_set)
                starting_search(filters, cof_list)
            elif (u == 2):
                filters = menu_filter_choose(main_filter_list)
                starting_search(filters, main_filter_list)
                b = True
            elif (u == 3):
                b = True
                return main_filter_list
        else:
            print('Такого номера нет')
            b = False

    #print("3. Сбросить фильтры и использовать далее исходный?")

#with open("./coffee_dataset.csv", 'r') as file:
#  csvreader = csv.reader(file)
#  coffe_set = list(csvreader)

#filters = menu_filter_choose(coffe_set)
#starting_search(filters, coffe_set)