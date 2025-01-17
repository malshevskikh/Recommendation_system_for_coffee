import csv
from operator import itemgetter, attrgetter, methodcaller
from geopy.distance import geodesic as GD
import tree_st
import re


countries = {}
Brazil = (-21.702367, -48.784556)
Columbia = (4.830098, -75.014173)
Sumatra = (-1.712501, 103.092568)
Kenia = (-0.234661, 36.751953)
Efiopia = (8.231351, 37.091604)
Indonesia = (-1.205029, 112.730740)
Ruanda = (-1.885288, 30.148379)
CostaRica = (9.786770, -83.654146)
Mexico = (18.371434, -98.559723)
Gwatemala = (14.662704, -91.020791)
Vietnam = (12.167967, 107.738022)
Uganda = (0.688563, 31.044344)
countries["Бразилия"] = (-21.702367, -48.784556)
countries["Колумбия"] = (4.830098, -75.014173)
countries["Суматра"] = (-1.712501, 103.092568)
countries["Кения"] = (-0.234661, 36.751953)
countries["Эфиопия"] = (8.231351, 37.091604)
countries["Индонезия"] = (-1.205029, 112.730740)
countries["Руанда"] = (-1.885288, 30.148379)
countries["Коста-Рика"] = (9.786770, -83.654146)
countries["Мексика"] = (18.371434, -98.559723)
countries["Гватемала"] = (14.662704, -91.020791)
countries["Вьетнам"] = (12.167967, 107.738022)
countries["Уганда"] = (0.688563, 31.044344)


#Бразилия, Колумбия, Суматра, Кения, Эфиопия, Индонезия, Руанда, Коста-Рика, Мексика, Гватемала, Вьетнам, Уганда

def calculate_lenght(tree, taste):
  way = []
  for i in tree:
    #print(i)
    #print("виаво: ", i[len(i) - 1], "(", type(i[len(i) - 1]),")","=", taste, "(", type(taste), ")")
    if taste == i[len(i) - 1]:
      #print("!!!!", taste, i[len(i) - 1])
      way = i
  length_of_way = 0
  for i in way:
    #print(i)
    length_of_way = length_of_way + 1
  return (way, length_of_way)

def calculate_way_between(tree, way_frist, way_second):
  way_between = 0
  d = len(tree)
  first = 0
  second = 0
  for i in range(1, d):
    if (way_frist == way_second):
      way_between = 0
    elif (tree[i] == way_frist):
      first = i
    elif (tree[i] == way_second):
      second = i
  #print("первый:", first, "второй:", second)
  way_between = abs(first - second)
  #print("расстояние:", way_between)
  return way_between

tree = tree_st.tree

def making_coord(countr, name_of_country):
  global sec_coord
  for i in countr:
    if name_of_country == i:
      sec_coord = countr[i]
  return sec_coord

def choose_coffee(set_of_coffee):
  global first_coffee
  d = len(set_of_coffee)
  #print(d)
  if set_of_coffee[0][0] == 'Название кофе':
    for i in range(1, d):
      print("Кофе №", i, "-", set_of_coffee[i][0])
  else:
    с = 1
    for i in range(0, d):
      print("Кофе №", с, "-", set_of_coffee[i][0])
      с = с + 1

  num_first_coffee = input('Выберите кофе под номером №: ')
  if (num_first_coffee.isdigit() == True):
    num_first_coffee = int(num_first_coffee)
    if set_of_coffee[0][0] == 'Название кофе':
      if (1 <= num_first_coffee <= d):
        m = True
        first_coffee = set_of_coffee[num_first_coffee]
      else:
        m = False
    else:
      if (1 <= num_first_coffee <= d):
        m = True
        first_coffee = set_of_coffee[num_first_coffee - 1]
      else:
        m = False
  else:
    m = False
  #print(m)
  while m == False:
    num_first_coffee = input('Такого номера нет в спике, выберите номер из списка: ')
    if (num_first_coffee.isdigit() == True):
      num_first_coffee = int(num_first_coffee)
      if (1 <= num_first_coffee <= d):
        m = True
        first_coffee = set_of_coffee[num_first_coffee]
  print("Вы выбрали:", first_coffee[0])

def choose_list_of_coffee(set_of_coffee, ar):
  global first_coffee
  d = len(set_of_coffee)
  like_dislike = []
  for i in range(1, d):
    print("Кофе №", i, "-", set_of_coffee[i][0])
  if ar == 2:
    a = False
    list_of_like_coffee = []
    while (a == False):
      list_num_of_coffee = input('Выберите и перечислите номера кофе через пробел для добавления в список лайков: ')
      numbers = list_num_of_coffee.split(' ')
      for i in numbers:
        if (i.isdigit() == True):
          if  (1 <= int(i) <= 46):
            list_of_like_coffee.append(set_of_coffee[int(i)])
            d = len(numbers)
            if i == numbers[d-1]:
              a = True
          else:
            a = False
            print("№", i, "нет в списке")
        else:
          a = False
          print("№", i, "нет в списке")
      if len(list_of_like_coffee) != len(numbers):
        a = False
        list_of_like_coffee = []
    #numbers = re.findall(r'\d+', list_of_coffee, flags=re.ASCII)
    #print(list_of_like_coffee)
    like_dislike = list_of_like_coffee
  elif ar == 3:
    #print("list_of_coffee")
    a = False
    b = False
    list_of_like_coffee = []
    list_of_dislike_coffee = []
    while (a == False):
      list_num_of_coffee = input('Выберите и перечислите номера кофе через пробел для добавления в список лайков: ')
      numbers = list_num_of_coffee.split(' ')
      for i in numbers:
        if (i.isdigit() == True):
          if  (1 <= int(i) <= 46):
            list_of_like_coffee.append(set_of_coffee[int(i)])
            d = len(numbers)
            if i == numbers[d-1]:
              a = True
          else:
            a = False
            print("№", i, "нет в списке")
        else:
          a = False
          print("№", i, "нет в списке")
      if len(list_of_like_coffee) != len(numbers):
        a = False
        list_of_like_coffee = []

    while (b == False):
      list_num_of_coffee = input('Выберите и перечислите номера кофе через пробел для добавления в список дизлайков: ')
      numbers = list_num_of_coffee.split(' ')
      for i in numbers:
        if (i.isdigit() == True):
          if (1 <= int(i) <= 46):
            list_of_dislike_coffee.append(set_of_coffee[int(i)])
            d = len(numbers)
            if i == numbers[d - 1]:
              b = True
          else:
            b = False
            print("№", i, "нет в списке")
        else:
          b = False
          print("№", i, "нет в списке")
      if len(list_of_dislike_coffee) != len(numbers):
        b = False
        list_of_dislike_coffee = []

    #print(list_of_like_coffee)
    #print(list_of_dislike_coffee)
    like_dislike.append(list_of_like_coffee)
    like_dislike.append(list_of_dislike_coffee)

  return like_dislike

def choose_proximity_measure():
  global proximity_measure
  print("Выберите меру близости для сравнения 2-х объектов датасета")
  print("1. Мера близости по граммовке кофе (модуль разности)")
  print("2. Мера близости по степени обжраки кофе(от светлой к темной)")
  print("3. Мера близости по географическому расположению стран, где произрастает кофе")
  print("4. Мера близости по дереву/ассоциатиная мера близости")
  print("5. Общая мера близости, которая учитывает все вышеупомянутые меры")
  proximity_measure = input('Выберите меру близости от 1 до 5: ')
  if (proximity_measure.isdigit() == True):
    proximity_measure = int(proximity_measure)
    if (proximity_measure ==1 or proximity_measure == 2 or proximity_measure== 3 or proximity_measure== 4 or proximity_measure== 5):
      m = True
    else:
      m = False
  else:
    m = False
  #print(m)
  while m == False:
    proximity_measure = input('Такого номера нет в спике, выберите меру близости от 1 до 5: ')
    if (proximity_measure.isdigit() == True):
      proximity_measure = int(proximity_measure)
      if (proximity_measure == 1 or proximity_measure == 2 or proximity_measure== 3 or proximity_measure== 4 or proximity_measure== 5):
        m = True
    #print(type(proximity_measure))
  return proximity_measure



#мера близости по граммовке кофе
def weight_mera(set_of_coffee, first_coffee):
  print("---------------------------------------------------------------------------------------------")
  print("Мера близости по граммовке упаковок кофе")
  #print(first_coffee)
  #print(second_coffee)
  grf = first_coffee[2]
  grf = int(grf)
  print("Вес упаковки кофе", first_coffee[0], "-", grf, "грамм")
  #diff= abs(grf - grs)
  #print("Модуль разности -", diff)
  l = []
  d = len(set_of_coffee)
  for i in range(1, d):
    time_list = ()
    #time_list.append(set_of_coffee[i][0])
    diff = abs(int(set_of_coffee[i][2]) - grf)
    #time_list.append(diff)
    time_list = (first_coffee[0], set_of_coffee[i][0], diff)
    l.append(time_list)
  dl = len(l)
  #for i in l:
    #print(i)
  sort = sorted(l, key=itemgetter(2))
  print("Модуль разности граммовки выбранного кофе со всеми из списка:")
  k = 0
  for i in sort:
    k+=1
    print("№", k, i[0], ",", i[1], "-", i[2])
  #for i in l:
  #print(i[2])

  return l

#мера близости по степени обжарки кофе
def degree_of_roast(set_of_coffee, first_coffee):
  print("---------------------------------------------------------------------------------------------")
  print("Мера близости по степени обжарки кофе")
  roastf = first_coffee[3]
  d = len(set_of_coffee)
  l = []
  exc = []
  for i in range(1, d):
    t = ()
    if (roastf == set_of_coffee[i][3]):
      t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 0)
      exc.append(0)
      #exc.append(3)
    else:
      if (roastf == 'светлая'):
        if (set_of_coffee[i][3] == 'средняя'):
          t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 5)
          exc.append(5)
          #exc.append(2)
        elif (set_of_coffee[i][3] == 'темная'):
          t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 10)
          exc.append(10)
          #exc.append(1)
      elif (roastf == 'средняя'):
        if (set_of_coffee[i][3] == 'светлая' or set_of_coffee[i][3] == 'темная'):
          t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 5)
          exc.append(5)
          #exc.append(2)
      elif (roastf == 'темная'):
        if (set_of_coffee[i][3] == 'средняя'):
          t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 5)
          exc.append(5)
          #exc.append(2)
        elif (set_of_coffee[i][3] == 'светлая'):
          t = (first_coffee[0], roastf, set_of_coffee[i][0], set_of_coffee[i][3], 10)
          exc.append(10)
          #exc.append(1)
    l.append(t)
  #print(l)
  print("Обжарка", first_coffee[0], "-", roastf)
  #k = 0
  #for i in l:
  #  k += 1
  #  print("№", k, i[0], "(",i[1],")",",", i[2], "(",i[3],")","-", i[4])

  #for i in l:
  #  print(i[4])

  sort = sorted(l, key=itemgetter(4))
  print("Отсортированный список кофе при выбранной мере блзости по степени обжарки:")
  k = 0
  for i in sort:
    k += 1
    print("№", k, i[0], ",", i[2], "-", i[4])

  return l





#мера близости по геограчискому расположение стран, где произрастает кофе
def geo_location(set_of_coffee, first_coffee, countr):
  print("---------------------------------------------------------------------------------------------")
  print("Мера близости по геограчискому расположение стран, где произрастает кофе")
  #print(first_coffee)
  #print(countr)
  coord_of_choosen_cof = making_coord(countr, first_coffee[4])

  print("Координаты страны", first_coffee[4], ":", coord_of_choosen_cof)

  d = len(set_of_coffee)
  l = []
  for i in range(1, d):
    t = ()
    #print(set_of_coffee[i][4])
    coord_of_another_cof = making_coord(countr, set_of_coffee[i][4])
    dis = GD(coord_of_choosen_cof, coord_of_another_cof).km
    t = (set_of_coffee[i][0], set_of_coffee[i][4], dis)
    l.append(t)
  #print(l)
  k = 0
  print("Расстояние между страной произротсания, выбранного кофе и всеми остальными")
  for i in l:
    k += 1
    print("№", k, i[0], "(", i[1], ")", "-", i[2], "км")

  #for i in l:
  #  print(i[2])

  sort = sorted(l, key=itemgetter(2))
  print("Отсортированный список кофе при выбранной мере блзости по расстоянию :")
  k = 0
  for i in sort:
    k += 1
    print("№", k, first_coffee[0], ",", i[0], "-", i[2])

  return l

  #print("The distance between New York and Texas is: ", GD(Niger, Vietnam).km)

#Мера близости по дереву/ассоциатиная мера близости
def tree_mer_bliz(set_of_coffee, tree, f_cof):
  print("---------------------------------------------------------------------------------------------")
  print("Мера близости по дереву/ассоциатиная мера близости")
  #print(len(tree))
  tastes = f_cof[1]

  z = tastes.find(",")

  l_elem = []
  f_elem = ()
  final = []

  if z == -1:
    f_elem = calculate_lenght(tree, tastes)
  else:
    #tastes = tastes[:-1].replace(',', '').split()
    tastes = tastes.split(', ')
    #print(tastes)
    for i in tastes:
      #print(i)
      elem = calculate_lenght(tree, i)
      l_elem.append(elem)
      #print(elem)

  if (l_elem == []):

    list_of_ways = []
    set_of_coffee = set_of_coffee[1:]
    for i in set_of_coffee:
      #print(i[0])
      #print("half", half_of_final)
      z = i[1].find(",")
      # print(z)
      count_of_ways = 0

      if z == -1:
        list_of_values_of_ways = []
        list_of_values_of_ways.append(f_cof[0])
        list_of_values_of_ways.append(f_cof[1])
        list_of_values_of_ways.append(i[0])
        list_of_values_of_ways.append(i[1])
        list_of_ways = []
        list_of_ways.append(tastes)
        #print(i)
        s_elem = calculate_lenght(tree, i[1])
        #print("Первый и Второй элементы", f_elem, s_elem)
        vr = calculate_way_between(tree, f_elem[0], s_elem[0])
        count_of_ways = count_of_ways + vr
        #print(f_elem, s_elem, count_of_ways)
        r = len(s_elem[0])
        #print(s_elem[0][r-1])
        list_of_ways.append(s_elem[0][r-1])
        #list_of_ways.append(count_of_ways)
        list_of_ways.append(vr)
        #print(list_of_ways)
        list_of_values_of_ways.append(list_of_ways)
        #print(list_of_values_of_ways)
        final.append(list_of_values_of_ways)
      #несколько вкусов у 2-го кофе
      else:
        sec_t = i[1].split(', ')
        #print("первый и второй элементы: ", f_elem, sec_t)
        list_num_1 = []
        #print("список вкусов вот такой:", sec_t)
        list_num_1.append(f_cof[0])
        list_num_1.append(f_cof[1])
        list_num_1.append(i[0])
        list_num_1.append(i[1])
        for j in sec_t:
          list_of_ways_second = []
          list_of_ways_second.append(tastes)
          s_elem = calculate_lenght(tree, j)
          #print("dfjefknjekmfl", f_elem, s_elem)
          vr = calculate_way_between(tree, f_elem[0], s_elem[0])
          count_of_ways = count_of_ways + vr
          list_of_ways_second.append(j)
          list_of_ways_second.append(count_of_ways)
          list_num_1.append(list_of_ways_second)
        final.append(list_num_1)
        #print("а вот и он: ",list_num_1)

    print("Данные выбранного кофе:", f_cof)
    print("---------------------------------------------------------------------------------")
    print("Сравнение вкусов, выбранного кофе, со вкусами остальных кофе")
    for i in final:
      print(i)
       # print("первый и второй элементы: ", f_elem, sec_t)

  # проверка на несколько вкусов
  elif (l_elem != []):

    #print(l_elem)
    list_of_values_of_coffee = []
    set_of_coffee = set_of_coffee[1:]

    for k in l_elem:
      #print(k)
      list_of_ways = []

      for i in set_of_coffee:
        # print(i[0])
        # print("half", half_of_final)
        z = i[1].find(",")
        # print(z)
        count_of_ways = 0

        # final.append(i[0])
        # final.append(i[1])

        # проверка на 1 вкус у 2-го кофе
        if z == -1:
          list_of_values_of_ways = []
          list_of_values_of_ways.append(f_cof[0])
          list_of_values_of_ways.append(f_cof[1])
          list_of_values_of_ways.append(i[0])
          list_of_values_of_ways.append(i[1])
          list_of_ways = []

          j = len(k[0])
          list_of_ways.append(k[0][j-1])
          #list_of_ways.append(tastes)
          #print("ВКУУУУУССС:", k[0][j-1])
          # print(i)

          s_elem = calculate_lenght(tree, i[1])
          # print("Первый и Второй элементы", f_elem, s_elem)
          vr = calculate_way_between(tree, k[0], s_elem[0])
          count_of_ways = count_of_ways + vr
          #print(k, s_elem, count_of_ways)
          r = len(s_elem[0])
          # print(s_elem[0][r-1])
          list_of_ways.append(s_elem[0][r - 1])
          list_of_ways.append(vr)
          #print(list_of_ways)
          list_of_values_of_ways.append(list_of_ways)
          #print(list_of_values_of_ways)
          final.append(list_of_values_of_ways)
          #print("vr:", vr)
          #print("count", count_of_ways)
        # несколько вкусов у 2-го кофе
        else:
          sec_t = i[1].split(', ')
          # print("первый и второй элементы: ", f_elem, sec_t)
          list_num_1 = []
          #print("список вкусов вот такой:", sec_t)
          list_num_1.append(f_cof[0])
          list_num_1.append(f_cof[1])
          list_num_1.append(i[0])
          list_num_1.append(i[1])
          for j in sec_t:
            list_of_ways_second = []

            q = len(k[0])

            #list_of_ways_second.append(k[0][j - 1])
            # list_of_ways.append(tastes)
            #print("ВКУУУУУССС:", k[0][q - 1])

            list_of_ways_second.append(k[0][q - 1])


            s_elem = calculate_lenght(tree, j)
            # print("dfjefknjekmfl", f_elem, s_elem)
            vr = calculate_way_between(tree, k[0], s_elem[0])
            count_of_ways = count_of_ways + vr
            list_of_ways_second.append(j)
            list_of_ways_second.append(vr)
            list_num_1.append(list_of_ways_second)
          final.append(list_num_1)
          #print("а вот и он: ", list_num_1)


    print("Данные выбранного кофе:", f_cof)
    print("---------------------------------------------------------------------------------")
    print("Сравнение вкусов, выбранного кофе, со вкусами остальных кофе")
    for i in final:
      print(i)
        # print("первый и второй элементы: ", f_elem, sec_t)


  #print(f_cof)
  #print(tastes)
  v = []
  if (l_elem == []):
    for i in final:
      list_of_count = []
      list_of_count.append(i[0])
      list_of_count.append(i[2])
      #print("first names:", list_of_count)
      count = 0
      # print("i:", i)
      for j in range(4, len(i)):
        # print("цалуклду:", i[j])
        count = count + i[j][2]
      list_of_count.append(count)
      #print("second names:", list_of_count)
      #v.append(list_of_count)
      s1 = []
      s2 = []
      tastes1 = i[1].split(', ')
      tastes2 = i[3].split(', ')
      #print("вкус1:", tastes1)
      #print("вкус2:", tastes2)
      s1 = len(tastes1)
      s2 = len(tastes2)
      s_obch = abs(s2 - s1)
      count_of_tastes = 0
      for k in tastes1:
        #print("k", k)
        for l in tastes2:
          #print("l", l)
          if (k != l):
            count_of_tastes = count_of_tastes + 1
          #print(count_of_tastes)
      #print(i[0], i[2], s_obch, count_of_tastes)
      list_of_count.append(count_of_tastes)
      v.append(list_of_count)

    print("---------------------------------------------------------------------------------")
    print("Название выбранного кофе | название 2-го кофе | сумма длин между вкусами | число несовпавших вкусов")
    for i in v:

      print(i)

  elif (l_elem != []):
    #print("ffff")
    vremenni_list = []
    list_of_count = []
    for i in final:
      #print("ssfef")

      if (i[2] not in vremenni_list):
        #print("jsfeijf", i[2])
        vremenni_list.append(i[2])

        list_of_count = []
        list_of_count.append(i[0])
        list_of_count.append(i[2])
        # print("first names:", list_of_count)
        count = 0
        # print("i:", i)
        for j in range(4, len(i)):
          # print("цалуклду:", i[j])
          count = count + i[j][2]
        list_of_count.append(count)
        #print("second names:", list_of_count)
        # v.append(list_of_count)
        s1 = []
        s2 = []
        tastes1 = i[1].split(', ')
        tastes2 = i[3].split(', ')
        # print(tastes1)
        # print(tastes2)
        s1 = len(tastes1)
        s2 = len(tastes2)
        s_obch = abs(s2 - s1)
        count_of_tastes = 0
        if s2 > s1:
          s3 = list(set(tastes2) - set(tastes1))
        elif s1 >= s2:
          s3 = list(set(tastes1) - set(tastes2))
        count_of_tastes = len(s3)
        list_of_count.append(count_of_tastes)
        v.append(list_of_count)

      elif (i[2] in vremenni_list):
        #print("------------")

        for j in v:
          if (j[1] == i[2]):
            #print("СОВПАЛО:::", j[1], "==", i[2])

            count = 0
            # print("i:", i)
            for n in range(4, len(i)):
              # print("цалуклду:", i[j])
              count = count + i[n][2]
            #print("oooowodosdowod%", count)
            j.append(count)

    print("---------------------------------------------------------------------------------")
    print("Название выбранного кофе | название 2-го кофе | сумма длин c 1-м вкусом выбранного кофе | число несовпавших вкусов | сумма длин со 2-м вкусом | ...")
    for i in v:
      print(i)

  victory = []

  for i in v:
    h = []
    h.append(i[0])
    h.append(i[1])
    #print(i[4])
    o = 0
    if len(i) > 4:
      for j in range(4, len(i)):
        o = o + i[j]
      #print(o)
    pro = (o + i[2]) * i[3]
    #print(pro)
    h.append(pro)
    victory.append(h)

  print("---------------------------------------------------------------------------------")
  print("Название выбранного кофе | название 2-го кофе | произведение суммы длин между вкусами и числа несовпавших вкусов")
  for i in victory:
    print(i)

  print("---------------------------------------------------------------------------------")
  victory2 = []
  for i in victory:
    t = ()
    t =(i[0], i[1], i[2])
    victory2.append(t)
  #print(victory2)
  #for i in victory:
  #  print(i[2])


  sort = sorted(victory2, key=itemgetter(2))
  k = 0
  print("Отсортированный список кофе при выбранной мере близости по дереву:")
  for i in sort:
    k += 1
    print("№", k, i[0], ",", i[1], "-", i[2])

  return victory



def menu_mera_blis(cof, tree, first_cof, countr):
  print("---------------------------------------------------------------------------------------------")
  print("Общая мера близости, включающая все остальные")
  r1 = weight_mera(cof, first_cof)
  r2 = degree_of_roast(cof, first_cof)
  r3 = geo_location(cof, first_cof, countr)
  r4 = tree_mer_bliz(cof, tree, first_cof)

  #привод меры №1 к 10-бальной оценке
  v1 = []
  minimum = r1[0][2]
  maximum = r1[0][2]
  for i in r1:
    if i[2] < minimum:
      minimum = i[2]
    if i[2] > maximum:
      maximum = i[2]
  #print("min=", minimum, "max=", maximum)
  obch = (maximum - minimum)/10
  #print(obch)
  for i in r1:
    w1 = []
    zn = i[2] // obch
    w1.append(first_cof[0])
    w1.append(i[1])
    w1.append(zn)
    v1.append(w1)

  #привод меры №2
  v2 = []
  for i in r2:
    w2 = []
    w2.append(first_cof[0])
    w2.append(i[2])
    w2.append(i[4])
    v2.append(w2)


  #привод меры №3 к 10-бальной оценке
  v3 = []
  minimum = r3[0][2]
  maximum = r3[0][2]
  for i in r3:
    if i[2] < minimum:
      minimum = i[2]
    if i[2] > maximum:
      maximum = i[2]
  #for i in r3:
  #  print(i)
  #print("min=", minimum, "max=", maximum)
  obch = (maximum - minimum)/10
  #print(obch)
  if maximum != minimum:
    for i in r3:
      w3 = []
      zn = i[2] // obch
      w3.append(first_cof[0])
      w3.append(i[0])
      w3.append(zn)
      v3.append(w3)
  else:
    for i in r3:
      w3 = []
      zn = obch
      w3.append(first_cof[0])
      w3.append(i[0])
      w3.append(zn)
      v3.append(w3)

  #привод меры №4 к 10-бальной оценке
  v4 = []
  minimum = r4[0][2]
  maximum = r4[0][2]
  for i in r4:
    if i[2] < minimum:
      minimum = i[2]
    if i[2] > maximum:
      maximum = i[2]
  #print("min=", minimum, "max=", maximum)
  obch = (maximum - minimum)/10
  #print(obch)
  for i in r4:
    w4 = []
    zn = i[2] // obch
    w4.append(first_cof[0])
    w4.append(i[1])
    w4.append(zn)
    v4.append(w4)

  d = len(v1)
  v5 =[]
  for i in range(0, d):
    w5 = ()
    #w5.append(first_cof[0])
    q = v1[i][2] + v2[i][2] + v3[i][2] + v4[i][2]
    #w5.append(v1[i][1])
    #w5.append(q)
    w5 = (first_cof[0], v1[i][1], q)
    v5.append(w5)

  print("----------------------------------------------------")
  print("Список сравнения выбранного кофе с остальными, обобщая все меры близости")
  for i in v5:
    print(i)

  print("----------------------------------------------------")
  print("Отсортированный список сравнения выбранного кофе с остальными, обобщая все меры близости")
  sort = sorted(v5, key=itemgetter(2))
  k = 0
  for i in sort:
    k += 1
    print("№", k, i[0], ",", i[1], "-", i[2])

  #for i in v5:
  #  print(i[2])

  return sort



def first_variant(coffe_set, countries, tree):
  # основная часть
  main_arr = []
  n = True
  while (n == True):
    choose_coffee(coffe_set)

    # print(proximity_measure)

    m = True
    while (m == True):
      choose_proximity_measure()
      if (proximity_measure == 1):
        main_arr = weight_mera(coffe_set, first_coffee)
      elif (proximity_measure == 2):
        main_arr = degree_of_roast(coffe_set, first_coffee)
      elif (proximity_measure == 3):
        main_arr = geo_location(coffe_set, first_coffee, countries)
      elif (proximity_measure == 4):
        main_arr = tree_mer_bliz(coffe_set, tree, first_coffee)
      elif (proximity_measure == 5):
        main_arr = menu_mera_blis(coffe_set, tree, first_coffee, countries)

      print("------------------------------------------------------------------------------------------------------------------")
      print("Новая мера близости c", first_coffee[0], "- 1")
      print("Новый кофе - 2")
      print("Заново выбрать новый пункт - 3")
      print("Закончить - 4")
      # print(u, type(u))
      b = False
      while (b == False):
        u = input("Выберите цифру от 1 до 4: ")
        if (u.isdigit() == True):
          u = int(u)
          if (u != 1 and u != 2 and u != 3 and u != 4):
            print('Такого номера нет в спике от 1 до 3')
            b = False
          elif (u == 1):
            m = True
            b = True
          elif (u == 2):
            n = True
            m = False
            b = True
          elif (u == 3):
            menu(coffe_set, countries, tree)
          elif (u == 4):
            m = False
            n = False
            b = True
            return main_arr
        else:
          print('Такого номера нет в спике от 1 до 4')
          b = False

def second_variant(coffe_set, countries, tree, ar, list_numbers_of_likes):
  main_arr = []
  arr_of_likes = []
  likes = []
  print(list_numbers_of_likes)
  print(coffe_set)
  g = len(coffe_set)
  if coffe_set[0][0] == 'Название кофе':
    for i in range(1, g):
      print(i, coffe_set[i], list_numbers_of_likes)
      if i in list_numbers_of_likes:
        likes.append(coffe_set[i])
  elif coffe_set[0][0] != 'Название кофе':
    list_numbers_of_likes_new = []
    for l in list_numbers_of_likes:
      list_numbers_of_likes_new.append(l - 1)
    list_numbers_of_likes = list_numbers_of_likes_new
    print("обновленный", list_numbers_of_likes_new)
    for i in range(0, g):
      print(i, coffe_set[i], list_numbers_of_likes)
      if i in list_numbers_of_likes:
        likes.append(coffe_set[i])
  #likes = choose_list_of_coffee(coffe_set, ar)

  f_likes = likes
  print("Лайкнутые объекты", likes)
  f = []
  for i in likes:
    #print(i)
    h = menu_mera_blis(coffe_set, tree, i, countries)
    f.append(h)

  likes = []
  for j in f:
    #print("ДО:", j)
    j = j[1:11]
    likes.append(j)
    #print("ПОСЛЕ:", j)
  f = []
  for i in likes:
    #print(i)
    for j in i:
      f.append(j)

  finaly = []
  t = ()
  for i in f:
    #print(i)
    c = 0
    for j in f:
      if i[1] == j[1]:
        c = c + 1
    t = (i[1], i[2], c)
    finaly.append(t)

  sort = sorted(finaly, key=itemgetter(2), reverse=True)

  vr = []
  mar = []
  for i in sort:
    if i[0] not in vr:
      t = (i[0], i[1], i[2])
      mar.append(t)
      vr.append(i[0])

  c1 = []
  c2 = []
  for i in mar:
    #print(i)
    if i[2] != 1:
      c1.append(i)
    else:
      c2.append(i)

  c2 = sorted(c2, key=itemgetter(1))

  c4 = []
  for i in c1:
    t = (i[0], i[2])
    c4.append(t)

  c3 = c1 + c2

  a1 = []
  a2 = []
  a3 = []
  print("---------------------------------------------------------------------------------------------------")
  print("Список лайков: ")
  for i in f_likes:
    print(i[0])
    if (i[0] not in a1):
      a1.append(i[0])
  print("Список из объектов, которые наиболее похожи на выбранные лайки")
  for i in c4:
    #print(i)
    if (i[0] not in a1):
      a2.append(i)
  for i in c2:
    #print(i)
    if (i[0] not in a1):
      a3.append(i)
  for i in a2:
    print(i)
  for i in a3:
    print(i)

  for i in a2:
    for j in coffe_set:
      if i[0] == j[0]:
        main_arr.append(j)
  for i in a3:
    for j in coffe_set:
      if i[0] == j[0]:
        main_arr.append(j)

  return main_arr



def third_variant(coffe_set, countries, tree, ar, list_numbers_of_likes, list_numbers_of_dislikes):
  main_arr = []

  arr_of_likes = []
  arr_of_dislikes = []
  g = len(coffe_set)
  if coffe_set[0][0] == 'Название кофе':
    for i in range(1, g):
      print(i, coffe_set[i], list_numbers_of_likes)
      if i in list_numbers_of_likes:
        arr_of_likes.append(coffe_set[i])
      if i in list_numbers_of_dislikes:
        arr_of_dislikes.append(coffe_set[i])
  elif coffe_set[0][0] != 'Название кофе':
    list_numbers_of_likes_new = []
    for l in list_numbers_of_likes:
      list_numbers_of_likes_new.append(l - 1)
    list_numbers_of_likes = list_numbers_of_likes_new
    list_numbers_of_dislikes_new = []
    for l in list_numbers_of_dislikes:
      list_numbers_of_dislikes_new.append(l - 1)
    list_numbers_of_dislikes = list_numbers_of_dislikes_new
    print("обновленные", list_numbers_of_likes_new, list_numbers_of_dislikes_new)
    for i in range(0, g):
      print(i, coffe_set[i], list_numbers_of_likes)
      if i in list_numbers_of_likes:
        arr_of_likes.append(coffe_set[i])
      if i in list_numbers_of_dislikes:
        arr_of_dislikes.append(coffe_set[i])



  #arr_of_likes = likes_and_dislikes[0]
  #arr_of_dislikes = likes_and_dislikes[1]
  #print("Лайкнутые и дизлайкнуые объекты", likes_and_dislikes)
  #for i in likes_and_dislikes:
  #  print(i)

  #создание списка объектов, похожих на выбранные для лайков
  f = []

  for i in arr_of_likes:
    print(i)
    h = menu_mera_blis(coffe_set, tree, i, countries)
    f.append(h)

  likes = []
  for j in f:
    # print("ДО:", j)
    j = j[1:11]
    likes.append(j)
    # print("ПОСЛЕ:", j)
  f = []
  for i in likes:
    # print(i)
    for j in i:
      f.append(j)

  # print("---------------------------------")
  finaly = []
  t = ()
  for i in f:
    # print(i)
    c = 0
    for j in f:
      if i[1] == j[1]:
        c = c + 1
    t = (i[1], i[2], c)
    finaly.append(t)

  sort = sorted(finaly, key=itemgetter(2), reverse=True)

  vr = []
  mar = []
  for i in sort:
    if i[0] not in vr:
      t = (i[0], i[1], i[2])
      mar.append(t)
      vr.append(i[0])


  c1 = []
  c2 = []
  for i in mar:
    # print(i)
    if i[2] != 1:
      c1.append(i)
    else:
      c2.append(i)

  c2 = sorted(c2, key=itemgetter(1))

  c4 = []
  for i in c1:
    t = (i[0], i[2])
    c4.append(t)

  c3 = c1 + c2


  print("--------------Список рекомендаци похожий на лайки-------------------")

  a1 = []
  a2 = []
  a3 = []

  for i in arr_of_likes:
    print(i[0])
    if (i[0] not in a1):
      a1.append(i[0])

  for i in c4:
    #print(i)
    if (i[0] not in a1):
      a2.append(i)
  for i in c2:
    #print(i)
    if (i[0] not in a1):
      a3.append(i)

  not_c3 = c3
  c3 = []
  for i in not_c3:
    if (i[0] not in a1):
      c3.append(i)

  #print("iwncxiwcioxwkcnwknckwncnwkcxm")
  #for i in not_c3:
  #  print(i)
  #print("--------------")
  #for i in c3:
  #  print(i)

  #print(arr_of_dislikes)
  vr = []
  for i in arr_of_dislikes:
    if i[0] not in vr:
      vr.append(i[0])
  #print(vr)
  arr = []

  for j in c3:
    if (j[0] not in vr):
      arr.append(j)
  print("---------------Исключение объектов-дизлайков из списка---------------")
  for i in arr:
    print(i)

  # создание списка объектов, похожих на выбранные для дизлайков

  f = []
  for i in arr_of_dislikes:
    #print(i)
    h = menu_mera_blis(coffe_set, tree, i, countries)
    f.append(h)
  likes = []
  for j in f:
    # print("ДО:", j)
    j = j[1:6]
    likes.append(j)
    # print("ПОСЛЕ:", j)
  f = []
  for i in likes:
    # print(i)
    for j in i:
      f.append(j)

  # print("---------------------------------")
  finaly = []
  t = ()
  for i in f:
    # print(i)
    c = 0
    for j in f:
      if i[1] == j[1]:
        c = c + 1
    t = (i[1], i[2], c)
    finaly.append(t)

  sort = sorted(finaly, key=itemgetter(2), reverse=True)

  vr = []
  mar = []
  for i in sort:
    if i[0] not in vr:
      t = (i[0], i[1], i[2])
      mar.append(t)
      vr.append(i[0])

  c1 = []
  c2 = []
  for i in mar:
    # print(i)
    if i[2] != 1:
      c1.append(i)
    else:
      c2.append(i)

  c2 = sorted(c2, key=itemgetter(1))

  c6 = []
  for i in c1:
    t = (i[0], i[2])
    c6.append(t)

  c5 = c1 + c2

  print("--------------Список лайков--------------")
  for i in arr_of_likes:
    print(i[0])


  print("--------------Список реколмендаций, основанный на лайках-------------------")
  for i in a2:
    print(i)
  for i in a3:
    print(i)

  print("--------------Список дизлайков--------------")
  for i in arr_of_dislikes:
    print(i[0])

  print("--------------Список рекомендаций, основанный на дизлайках-------------------")
  #for i in c5:
  #  print(i)

  #print("---------")
  for i in c6:
    print(i)
  for i in c2:
    print(i)


  #Исключение из списка рекомедацией объектов похожие на дизлайки
  vr = []
  for i in c5:
    if i[0] not in vr:
      vr.append(i[0])

  final_yes = []
  for j in c3:
    if j[0] not in vr:
      final_yes.append(j)

  print("--------------Список лайков, из которого удалены объекты похожие на дизлайки-------------------")
  #for i in final_yes:
  #  print(i)

  final_yes1 = []
  final_yes2 = []
  for i in final_yes:
    # print(i)
    if i[2] != 1:
      final_yes1.append(i)
    else:
      final_yes2.append(i)


  final_yes2 = sorted(final_yes2, key=itemgetter(1))


  final_yes3 = []
  for i in final_yes1:
    t = (i[0], i[2])
    final_yes3.append(t)

  for i in final_yes3:
    print(i)
  for i in final_yes2:
    print(i)

  for i in final_yes3:
    for j in coffe_set:
      if i[0] == j[0]:
        main_arr.append(j)
  for i in final_yes2:
    for j in coffe_set:
      if i[0] == j[0]:
        main_arr.append(j)

  return main_arr



#with open("./coffee_dataset.csv", 'r') as file:
#  csvreader = csv.reader(file)
#  coffe_set = list(csvreader)


def menu (coffe_set, countries, tree):
  main_arr = []
  print("------------------------------------------------------------------------------------------------------------------")
  print("Выберите необходимый пункт")
  print("Рекомендация на основе 1-го объекта (кофе) - 1")
  print("Рекомендация на основе массива лайкнутых объектов (кофе) - 2")
  print("Рекомендация на основе массива лайкнутых и дизлайкнутых объектов (кофе) - 3")
  print("Закончить - 4")
  b = False
  while (b == False):
    u = input("Укажите цифру от 1 до 4: ")
    if u.isdigit() == True:
      u = int(u)
      if (u != 1 and u != 2 and u != 3 and u != 4):
        print('Такого номера нет в спике от 1 до 4')
        b = False
      elif (u == 1):
        main_arr = first_variant(coffe_set, countries, tree)
        b = True
      elif (u == 2):
        main_arr = second_variant(coffe_set, countries, tree, u)
        b = True
      elif (u == 3):
        main_arr = third_variant(coffe_set, countries, tree, u)
        b = True
      elif (u == 4):
        b = True
    else:
      print('Такого номера нет в спике от 1 до 4')
      b = False

  return main_arr

#menu(coffe_set, countries, tree)
#first_variant(coffe_set, countries, tree)


#bin_mer_vliz(coffe_set)

