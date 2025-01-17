import csv
from operator import itemgetter, attrgetter, methodcaller
from geopy.distance import geodesic as GD
import tree_st
import re
import lab3, lab4_2, lab3_2
from lab3 import countries, tree
import patterns_for_regex


def make_uniq_list(taste_list):
    time_list = []
    #print("taste_list", taste_list)
    t = taste_list[0]
    for i in range(len(t)):
        #print(t[i])
        if (t[i] not in time_list) and (t[i] != '') and (t[i] != "ом"):
            time_list.append(t[i])
    #print("финал", time_list)
    return time_list

def make_normal_list(stup_list):
    final_list = []
    short_tastes = patterns_for_regex.short_tastes
    for i in stup_list:
        d = i[0]
        for j in short_tastes:
            #print(j)
            if d in j:
                print("i", i[0])
                print(j)
                final_list.append(j[len(j) - 1])
            #for k in j:
            #    if j == i[0]:
            #        final_list.append(j[len(j)-1])
    print(final_list)
    return final_list

def make_normal_list_count(stup_list):
    final_list = []
    short_count = patterns_for_regex.short_country
    for i in stup_list:
        d = i[0]
        for j in short_count:
            #print(j)
            if d in j:
                print("i", i[0])
                print(j)
                final_list.append(j[len(j) - 1])
            #for k in j:
            #    if j == i[0]:
            #        final_list.append(j[len(j)-1])
    print(final_list)
    return final_list

def make_numbers(num):
    d = len(num) - 1
    b = 0
    for i in num:
        b = b + int(i) * (10**d)
        d = d - 1
    print(b)
    return b

def take_tatses(l):
    print("sdf")


def questiona_sentence(stringS, coffe_set):
    print("Просто вопросительное")
    arr_of_req = []
    delice_filter_list = []
    weight_filter_list = []
    obg_filter_list = []
    countries_filter_list = []
    sort_filter_list = []
    obgarka = re.search("(?:обжарк)|(?:светл)|(?:средн)|(?:темн)", stringS)
    country1 = re.search("(?:стран)|(?:регион)", stringS)
    country2 = re.search("((?:Бразили)|(?:Колумби)|(?:Суматр)|(?:Кени)|(?:Суматр)|(?:Эфиопи)|(?:Индонези)|(?:Руанд)|(?:Коста-Рик)|(?:Мексик)|(?:Гватемал)|(?:Вьетнам)|(?:Уганд))", stringS)
    gramm = re.search("(?:грамм)|(?:вес)|(?:упаковк)|(?:пачк)", stringS)
    delice = re.search("(?:вкус)", stringS)
    sort = re.search("(?:сорт)|(?:робуст[а|ы])|(?:арабик[а|и])", stringS)
    Yes = False
    first_patterns = patterns_for_regex.patterns
    for i in first_patterns:
        equel_to_del = re.search(i, stringS)
        if equel_to_del:
            Yes = True
    if delice or Yes:
        print("функция которая берет вкусы из строки")
        patterns = patterns_for_regex.patterns
        с = 0
        fr = []
        for i in patterns:
            equel_to_delice = re.search(i, stringS)
            if equel_to_delice:
                с = с + 1
                find_to_delice = re.findall(i, stringS)
                u = make_uniq_list(find_to_delice)
                fr.append(u)
        print(с, "вкусов")
        print(fr)
        final = make_normal_list(fr)
        delice_filter_list = lab4_2.delice_filter(coffe_set, final)
        #print(delice_filter_list)
        arr_of_req.append(delice_filter_list)



    if gramm:
        print("функция которая берет вес из строки")
        more_wight = re.search("((?:больше)|(?:не)\s(?:менее))\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])", stringS)
        less_weight = re.search("((?:меньше)|(?:не)\s(?:более))\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])", stringS)
        between_weight1 = re.search("(?:между)\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])(?:\s|\sи\s)([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])", stringS)
        between_weight2 = re.search("((?:более)|(?:больше))\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])\sи\s((?:менее)|(?:меньше))\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])", stringS)
        weight_0 = None
        weight_1 = None

        very_little = re.search("(?:очень\sмаленьк((?:ий)|(?:ая)|(?:им)))", stringS)
        little = re.search("(?:маленьк((?:ий)|(?:ая)|(?:им)))", stringS)
        middle = re.search("(?:средн((?:ий)|(?:ее)|(?:им)))", stringS)
        not_big = re.search("(?:не\sочень\sбольш((?:ой)|(?:ая)|(?:им)))", stringS)
        big = re.search("(?:больш((?:ой)|(?:ая)|(?:им)))", stringS)

        if very_little:
            print("очень маленький")
            weight_0 = 0
            weight_1 = 137.5
        elif little:
            print("маленький")
            weight_0 = 138
            weight_1 = 237.5
        elif middle:
            print("средний")
            weight_0 = 238
            weight_1 = 750
        elif not_big:
            print("не очень большой")
            weight_0 = 751
            weight_1 = 1425
        elif big:
            print("большой")
            weight_0 = 1426
            weight_1 = 2500

        if more_wight and not less_weight and not between_weight1 and not between_weight2:
            print("Вес больше (число)")
            a = "(?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])"
            weight = re.findall(a, stringS)
            print(weight)
            weight_0 = make_numbers(weight)
        elif less_weight and not more_wight and not between_weight1 and not between_weight2:
            print("Вес меньше (число)")
            a = "(?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])"
            weight = re.findall(a, stringS)
            print(weight)
            weight_1 = make_numbers(weight)
        elif (between_weight1 or between_weight2):
            if between_weight1:
                print("Вес между ... и ...")
                #a = "((?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])\sи\s(?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]))"

                #a = "((?:между)\s([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9])\s(и))"
                q = stringS.split(' ')
                print(q)
                for i in range(len(q)):
                    if q[i] == 'между':
                        weight_0 = int(q[i+1])
                        weight_1 = int(q[i+3])
                #weight = re.findall(a, stringS)
                print(weight_0, weight_1)
            elif between_weight2:
                print("Вес больше ... и меньше ...")
                q = stringS.split(' ')
                print(q)
                for i in range(len(q)):
                    if q[i] == 'больше' or q[i] == 'более':
                        weight_0 = int(q[i + 1])
                    elif q[i] == 'меньше' or q[i] == 'менее':
                        weight_1 = int(q[i + 1])
                # weight = re.findall(a, stringS)
                print(weight_0, weight_1)
        print("вес № 1", "-", weight_0, ";", "вес № 2", "-", weight_1)
        weight_filter_list = lab4_2.weight_filter(coffe_set, weight_0, weight_1)
        #print(weight_filter_list)
        arr_of_req.append(weight_filter_list)


    if obgarka:
        print("функция которая берет обжарки из строки")
        light = re.search("(?:светл)", stringS)
        middle = re.search("(?:средн)", stringS)
        dark = re.search("(?:темн)", stringS)
        not_light = re.search("(?:не)\s(?:имеет)\s(?:светл)", stringS)
        not_middle = re.search("(?:не)\s(?:имеет)\s(?:средн)", stringS)
        not_dark = re.search("(?:не)\s(?:имеет)\s(?:темн)", stringS)
        obg = []
        if not_light:
            not_light_and_not_dark = re.search("(?:не)\s(?:имеет)\s(?:светлую)(,\s|\sи\s)(?:темн)", stringS)
            not_light_and_not_middle = re.search("(?:не)\s(?:имеет)\s(?:светлую)(,\s|\sи\s)(?:средн)", stringS)
            if not_light_and_not_dark and not not_light_and_not_middle:
                print("тут не светлая и не темная")
                obg = ["средняя"]
            elif not_light_and_not_middle and not not_light_and_not_dark:
                print("тут не светлая и не средняя")
                obg = ["темная"]
            elif not_light and not not_light_and_not_dark and not not_light_and_not_dark:
                print("тут не светлая обжарка")
                obg = ["темная", 'средняя']
        elif not_middle:
            not_middle_and_not_dark = re.search("(?:не)\s(?:имеет)\s(?:среднюю)(,\s|\sи\s)(?:темн)", stringS)
            not_middle_and_not_light = re.search("(?:не)\s(?:имеет)\s(?:среднюю)(,\s|\sи\s)(?:светл)", stringS)
            if not_middle_and_not_dark and not not_middle_and_not_light:
                print("тут не средняя и не темная")
                obg = ["светлая"]
            elif not_middle_and_not_light and not not_middle_and_not_dark:
                print("тут не средняя и не светлая")
                obg = ["темная"]
            elif not_middle and not not_middle_and_not_dark and not not_middle_and_not_light:
                print("тут не средняя обжарка")
                obg = ["темная", 'светлая']
        elif not_dark:
            not_dark_and_not_light = re.search("(?:не)\s(?:имеет)\s(?:темную)(,\s|\sи\s)(?:светл)", stringS)
            not_dark_and_not_middle = re.search("(?:не)\s(?:имеет)\s(?:темную)(,\s|\sи\s)(?:средн)", stringS)
            if not_dark_and_not_light and not not_dark_and_not_middle:
                print("тут не темная и не светлая")
                obg = ["средняя"]
            elif not_dark_and_not_middle and not not_dark_and_not_light:
                print("тут не темная и не средняя")
                obg = ["светлая"]
            elif not_dark and not not_dark_and_not_light and not not_dark_and_not_middle:
                print("тут только темная")
                obg = ["светлая", 'средняя']
        elif light:
            not_light = re.search("((?:не)\s(?:светл)|(?:не)\s(?:имеет)\s(?:светл))", stringS)
            if light and middle:
                print("тут светлая или средняя обжарки")
                obg = ["светлая", 'средняя']
            elif light and dark:
                print("тут светлая или темная обжарки")
                obg = ["светлая", 'темная']
            elif not_light:
                print("тут не светлая обжарка")
                obg = ["средняя", 'темная']
            elif light and not middle and not dark and not not_light:
                print("тут только светлая")
                obg = ["светлая"]
        elif middle:
            not_middle = re.search("((?:не)\s(?:средн)|(?:не)\s(?:имеет)\s(?:средн))", stringS)
            if middle and light:
                print("тут средняя или светлая обжарки")
                obg = ["светлая", 'средняя']
            elif middle and dark:
                print("тут средняя или темная обжарки")
                obg = ["темная", 'средняя']
            elif not_middle:
                print("тут не средняя обжарка")
                obg = ["светлая", 'темная']
            elif middle and not light and not dark and not not_middle:
                print("тут средняя обжарка")
                obg = ["средняя"]
        elif dark:
            not_dark = re.search("((?:не)\s(?:темн)|(?:не)\s(?:имеет)\s(?:темну))", stringS)
            if dark and light:
                print("тут темная или светлая обжарки")
                obg = ["темная", 'светлая']
            elif dark and middle:
                print("тут темная или средняя обжарки")
                obg = ["темная", 'средняя']
            elif not_dark:
                print("тут не темная обжарка")
                obg = ["светлая", 'средняя']
            elif dark and not light and not middle and not not_dark:
                print("тут только темная")
                obg = ["темная"]

        obg_filter_list = lab4_2.obg_filter(coffe_set, obg)
        #print(obg_filter_list)
        arr_of_req.append(obg_filter_list)

    if country1 or country2:
        print("функция которая берет страны из строки")
        one_country = re.search("(?:из)\s((?:Бразилии)|(?:Колумбии)|(?:Суматры)|(?:Кении)|(?:Суматры)|(?:Эфиопии)|(?:Индонезии)|(?:Руанды)|(?:Коста-Рики)|(?:Мексики)|(?:Гватемалы)|(?:Вьетнама)|(?:Уганды))(\?)", stringS)
        some_country = re.search("((?:Бразилии)|(?:Колумбии)|(?:Суматры)|(?:Кении)|(?:Суматры)|(?:Эфиопии)|(?:Индонезии)|(?:Руанды)|(?:Коста-Рики)|(?:Мексики)|(?:Гватемалы)|(?:Вьетнама)|(?:Уганды))(\,|\sи\s)", stringS)
        if one_country and not some_country:
            print("Из 1 страны")
        elif some_country:
            print("Из нескольких стран")

        patterns_country = patterns_for_regex.patterns_country
        ct = 0
        fr = []
        for i in patterns_country:
            equel_to_country = re.search(i, stringS)
            if equel_to_country:
                ct = ct + 1
                find_to_country = re.findall(i, stringS)
                print(find_to_country)
                #u = make_uniq_list(find_to_country)
                if find_to_country not in fr:
                    fr.append(find_to_country)
                #fr.append(u)
        print(ct, "стран")
        print(fr)
        countr_list = make_normal_list_count(fr)
        countries_filter_list = lab4_2.country_filter(coffe_set, countr_list)
        arr_of_req.append(countries_filter_list)

    if sort:
        #print("функция которая берет сорта из строки")
        arabic = re.search("(?:арабик)", stringS)
        robusta = re.search("(?:робуст)", stringS)
        n_arab = re.search("(?:не\sарабик)", stringS)
        n_rob = re.search("(?:не\sробуста)", stringS)
        sort_list = []
        if arabic and robusta:
            print("тут и арабика и робуста")
            sort_list = ["арабика", "робуста"]
        elif n_arab and n_rob:
            print("Сортов кроме арабики и робуста нет")
        elif arabic and not robusta:
            not_arabica = re.search("(?:не)\s(?:арабик)", stringS)
            if not_arabica:
                print("тут не арабика")
                sort_list = ["робуста"]
            else:
                print("тут арабика")
                sort_list = ["арабика"]
        elif robusta and not arabic:
            not_robusta = re.search("(?:не)\s(?:робуст)", stringS)
            if not_robusta:
                print("тут не робуста")
                sort_list = ["арабика"]
            else:
                print("тут робуста")
                sort_list = ["робуста"]
        sort_filter_list = lab4_2.sort_filter(coffe_set, sort_list)
        #print(sort_filter_list)
        arr_of_req.append(sort_filter_list)

    for i in arr_of_req:
        print(i)

    main_filter_list = lab4_2.compare_five_lists(arr_of_req)
    if main_filter_list == []:
        main_filter_list = coffe_set
        print("С учетом всех фильтров, список кофе получился пустым, поэтомк он не изменился")
    else:
        print("С учетом всех фильтров, вот список кофе:")

    d = len(main_filter_list)
    r = 1
    for i in range(0, d):
        print("Кофе №", r, "-", main_filter_list[i][0])
        r = r + 1
    return main_filter_list

def recommend_sentence(stringS, coffe_set):
    print("РЕКОМЕНДУЮ!")
    like = re.search("(?:похож(ий)?\sна)", stringS)
    diskike = re.search("(?:не\sпохож(ий)?\sна)", stringS)
    array_of_likes = []
    array_of_dislikes = []
    if like and not diskike:
        print("Только лайки")
        index_0 = 0
        t = re.split(' |, ', stringS)
        print(t)
        dl = len(t)
        for i in range(0, dl - 1):
            if (t[i] == "похож" or t[i] == "похожий") and t[i + 1] == "на":
                index_0 = i + 2
                print(index_0)
        for j in range(index_0, dl):
            if (t[j].isdigit() == True):
                array_of_likes.append(int(t[j]))
        #print(array_of_likes)
        #print(coffe_set)
        flag = True
        for i in array_of_likes:
            if not (1 <= i <= 46):
                print("номера", i, "нет в списке от 1 до 46")
                flag = False
        ar = 2
        result = lab3_2.second_variant(coffe_set, countries, tree, ar, array_of_likes)

    elif like and diskike:
        print("Только лайки и дизлайки")
        index_0 = 0
        index_1 = 0
        t = re.split(' |, ', stringS)
        print(t)
        dl = len(t)
        for i in range(0, dl - 1):
            if t[i] != "не" and (t[i + 1] == "похож" or t[i + 1] == "похожий") and t[i + 2] == "на":
                index_0 = i + 3
                print(index_0)
            if t[i] == "не" and (t[i + 1] == "похож" or t[i + 1] == "похожий") and t[i + 2] == "на":
                index_1 = i + 3
                print(index_1)
        if index_0 < index_1:
            for j in range(index_0, index_1 - 3):
                if (t[j].isdigit() == True):
                    array_of_likes.append(int(t[j]))
            for k in range(index_1, dl):
                if (t[k].isdigit() == True):
                    array_of_dislikes.append(int(t[k]))
        elif index_0 > index_1:
            for j in range(index_1, index_0 - 3):
                if (t[j].isdigit() == True):
                    array_of_likes.append(int(t[j]))
            for k in range(index_0, dl):
                if (t[k].isdigit() == True):
                    array_of_dislikes.append(int(t[k]))
        print(array_of_likes)
        print(array_of_dislikes)
        flag = True
        for i in array_of_likes:
            if not (1 <= i <= len(coffe_set)):
                print("номера", i, "нет в списке от 1 до", len(coffe_set))
                flag = False

        for i in array_of_dislikes:
            if not (1 <= i <= len(coffe_set)):
                print("номера", i, "нет в списке от 1 до", len(coffe_set))
                flag = False
        ar = 3
        result = lab3_2.third_variant(coffe_set, countries, tree, ar, array_of_likes, array_of_dislikes)
    return result

def output_list_of_coffe(coffe_set):
    d = len(coffe_set)
    r = 1
    for i in range(0, d):
        if coffe_set[i][0] != "Название кофе":
            print("Кофе №", r, "-", coffe_set[i][0])
            r = r + 1

def output_complex_list_of_coffe(coffe_set):
    d = len(coffe_set)
    r = 1
    for i in range(0, d):
        if coffe_set[i][0] != "Название кофе":
            print("Кофе №", r, "-", coffe_set[i])
            r = r + 1

def output_list_of_contries(coffe_set):
    out = []
    for i in coffe_set:
        if i[4] not in out:
            out.append(i[4])
    r = 1
    for j in out:
        print("№", r, "-", j)
        r = r + 1

def output_list_of_delices(coffe_set):
    out = []
    for i in coffe_set:
        if i[1] != 'вкус кофе':
            a = i[1].split(", ")
            #print(a)
            for j in a:
                if j not in out:
                    out.append(j)
    r = 1
    for k in out:
        print("№", r, "-", k)
        r = r + 1

def output_list_of_obg():
    print("№ 1 - светлая")
    print("№ 2 - средняя")
    print("№ 3 - темная")

def output_list_of_sort():
    print("№ 1 - арабика")
    print("№ 2 - робуста")


def queation_filter(stringS, coffe_set):
    print(stringS)
    exap0 = re.search("(?:кофе)|(?:вкус)|(?:сорт)|(?:стран)|(?:обжарк)|(?:грамм)", stringS)
    print(exap0)
    if exap0:
        exap1 = re.search("(?:[к|К]ак)|(?:[М|м]ож)|(?:[С|с]колько)|\?", stringS)
        exap2 = re.search("((?:[в|В]ыве((?:сти)|(?:ди)|(?:дите)))|(?:[Н|н]ай[д|т])|((?:((?:по)|(?:По)))?рекоменд((?:уй)|(?:уйте))))", stringS)
        exap3 = re.search("(?:похож(ий)?\sна)", stringS)
        if exap1 or exap2:
            if not exap3:
                coffe_set = questiona_sentence(stringS, coffe_set)
            elif exap3:
                coffe_set = recommend_sentence(stringS, coffe_set)
    else:
        print("Введите нормальный запрос!")
    return coffe_set


with open("./coffee_dataset.csv", 'r') as file:
  csvreader = csv.reader(file)
  old_coffe_set = list(csvreader)


coffe_set = old_coffe_set
stop = False
while stop == False:
    s = input("Введите запрос: ")
    end = re.search("(?:[зЗ]акончить)|(?:[Зз]авершить)|(?:[Кк]онец)", s)
    list_1 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sсписок\sкофе)", s)
    list_2 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sсписок\sстран)", s)
    list_3 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sсписок\sвкусов)", s)
    list_4 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sсписок\sобжарок)", s)
    list_5 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sсписок\sсортов)", s)
    list_6 = re.search("(?:[с|С]бро((?:сьте)|(?:сить))\sсписок\sкофе)", s)
    list_7 = re.search("(?:[в|В]ыве((?:сти)|(?:ди)|(?:дите))\sподробный\sсписок\sкофе)", s)
    if list_1:
        output_list_of_coffe(coffe_set)
    elif list_2:
        output_list_of_contries(coffe_set)
    elif list_3:
        output_list_of_delices(coffe_set)
    elif list_4:
        output_list_of_obg()
    elif list_5:
        output_list_of_sort()
    elif list_6:
        coffe_set = old_coffe_set
    elif list_7:
        output_complex_list_of_coffe(coffe_set)
    elif end:
        stop = True
    else:
        coffe_set = queation_filter(s, coffe_set)
