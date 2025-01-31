import csv

header = ['Название кофе', 'вкус кофе', 'число грамм', 'степень обжарки', 'страна произростания зерен', 'сорт кофе']
data = [

    #COSMIC LATTE
    ['БРАЗИЛИЯ САНТА МОНИКА', 'мёд, апельсин, тёмный виноград', 200, 'светлая', 'Бразилия', 'арабика'],
    ['КОЛУМБИЯ ЭЛЬ ВЕРГЕЛЬ', 'красный виноград, фиалка', 200, 'светлая', 'Колумбия', 'арабика'],
    ['СУМАТРА ИПАК ГАЙО', 'табачный лист, зеленые овощи, апельсин, корица', 200, 'светлая', 'Суматра', 'арабика'],
    ['КЕНИЯ МУГАГА АА', 'черная смородина, арбуз, земляника', 200, 'светлая', 'Кения', 'арабика'],
    ['КОЛУМБИЯ ХУАН ЧАМОРРО ВЕЛЕЗ', 'абрикос, варенье из черешни, карамель', 1000, 'темная', 'Колумбия', 'арабика'],

    #DOUBLE-B
    ['БРАЗИЛИЯ СЕМЬЯ ГАРСИЯ', 'слива, белая черешня, тростниковый сахар, гибискус', 50, 'светлая', 'Бразилия', 'арабика'],
    ['БРАЗИЛИЯ ВАЛЕ ДО СОЛ', 'тёмный виноград, горький шоколад, бейлиз', 200, 'светлая', 'Бразилия', 'арабика'],
    ['КЕНИЯ КИИ А', 'зелёное яблоко, персик, гибискус, тростниковый сахар', 200, 'светлая', 'Кения', 'арабика'],
    ['КЕНИЯ КОМОТАИ ГАТУЙИ АВ', 'лайм, крыжовник, чёрный чай, желтое яблоко', 200, 'светлая', 'Кения', 'арабика'],
    ['КОЛУМБИЯ РАФАЭЛЬ АЙА КАТУРРА 120', 'чернослив, шоколадный трюфель, черри-кола', 200, 'светлая', 'Колумбия', 'арабика'],
    ['ЭФИОПИЯ ЧЕЛБЕСА ДАНЧЕ', 'абрикос, лимон, бергамот, чёрный чай', 200, 'светлая', 'Эфиопия', 'арабика'],
    ['ЭФИОПИЯ ИДИДО', 'мандарин, персик, лемонграсс, молочный шоколад', 150, 'светлая', 'Эфиопия', 'арабика'],
    ['ИНДОНЕЗИЯ ФРИНСА ЛАКТИК ХАНИ', 'помело, красное яблоко, кокос', 200, 'светлая', 'Индонезия', 'арабика'],
    ['ИНДОНЕЗИЯ ФРИНСА ЛАКТИК', 'яблочный сидр, вяленый банан, сахар мусковадо', 200, 'светлая', 'Индонезия', 'арабика'],
    ['КОЛУМБИЯ РЕЙНАЛЬДО ЛОПЕС', 'красный виноград, темный шоколад, личи, лаванда', 200, 'светлая', 'Колумбия', 'арабика'],
    ['РУАНДА УБУМВЕ 96', 'чернослив в шоколаде, кумкват, желтый изюм, орех макадамия', 200, 'светлая', 'Руанда', 'арабика'],

    #Черный Кооператив
    ['Колумбия от Хуана Чаморро Велеза | эспрессо', 'сливочная карамель, желтая слива, груша', 1250, 'средняя', 'Колумбия', 'арабика'],
    ['Колумбия от Хуана Чаморро Велеза | фильтр', 'красное яблоко, китайская груша, сливочная карамель, чёрный чай', 200, 'светлая', 'Колумбия', 'арабика'],
    ['Эфиопия из Ураги | эспрессо', 'чёрный чай, слива, молочное печенье, карамель', 1000, 'светлая', 'Эфиопия', 'арабика'],
    ['Эфиопия из Ураги | фильтр', 'красный апельсин, белый виноград, специи', 200, 'светлая', 'Эфиопия', 'арабика'],

    #camera obscura coffee
    ['Бразилия Барра Эстейт', 'миндаль, карамель, шоколад', 1000, 'темная', 'Бразилия', 'арабика'],
    ['Эфиопия Челчеле: эспрессо', 'брусничное варенье, черника, лемонграсс', 1000, 'темная', 'Эфиопия', 'арабика'],
    ['Бразилия Фазенда Мариано', 'арахисовое пралине, какао', 250, 'светлая', 'Бразилия', 'арабика'],
    ['Эфиопия Гуджи Хадесо', 'красное яблоко, бергамот, чернослив', 250, 'светлая', 'Эфиопия', 'арабика'],
    ['Эфиопия Челчеле: фильтр', 'красное яблоко, соленая карамель, лемонграсс', 250, 'светлая', 'Эфиопия', 'арабика'],
    ['Кения Киамабара АА', 'черная смородина, арбузный сок, клубника', 250, 'светлая', 'Кения', 'арабика'],

    #west4 coffee
    ['Эфиопия Чамола и Хангади Вореда', 'персик, мандарин', 100, 'светлая', 'Эфиопия', 'арабика'],
    ['Индонезия Ява Фринса', 'клубничный ликёр, вяленый банан, желтое яблоко', 100, 'светлая', 'Индонезия', 'арабика'],
    ['Коста-Рика Пальмичаль', 'зелёное яблоко, карамбола', 100, 'светлая', 'Коста-Рика', 'арабика'],
    ['Мексика Муксбаль', 'чернослив', 100, 'светлая', 'Мексика', 'арабика'],
    ['Колумбия Эль Кармен Декаф', 'тростниковый сахар, мускатный орех', 100, 'светлая', 'Колумбия', 'арабика'],
    ['Кения Ньякуру', 'кизил, красная смородина, гранат', 100, 'светлая', 'Кения', 'арабика'],
    ['Колумбия Ла Индонесья', 'красное яблоко, чернослив', 100, 'светлая', 'Колумбия', 'арабика'],
    ['Эфиопия Данче', 'абрикос, бергамот', 100, 'светлая', 'Эфиопия', 'арабика'],
    ['Эспрессо Бразилия Да Лагоа', 'белый виноград, молочный шоколад', 1000, 'темная', 'Бразилия', 'арабика'],
    ['Эспрессо Эфиопия Декаф', 'чернослив', 1000, 'темная', 'Эфиопия', 'арабика'],
    ['Эспрессо Мексика Women Power', 'апельсиновое варенье, грецкий орех, темный шоколад', 200, 'темная', 'Мексика', 'арабика'],
    ['Эспрессо Руанда Киву', 'курага, изюм', 500, 'темная', 'Руанда', 'арабика'],

    #tasty coffee
    ['БРАЗИЛИЯ СЕРРАДО', 'жареные орехи, шоколад, карамель', 500, 'средняя', 'Бразилия', 'арабика'],
    ['ЭФИОПИЯ ИРГАЧЕФФ НАТ', 'молочный шоколад, грейпфрут', 1000, 'средняя', 'Эфиопия', 'арабика'],
    ['БРАЗИЛИЯ МОЖИАНА', 'фундук, какао', 1000, 'средняя', 'Бразилия', 'арабика'],
    ['ГВАТЕМАЛА ФЭНСИ', 'апельсин, молочный шоколад', 1000, 'средняя', 'Гватемала', 'арабика'],
    ['КОЛУМБИЯ БОГОТА', 'тёмный виноград, красное яблоко, горький шоколад', 1500, 'средняя', 'Колумбия', 'арабика'],

    #РОБУСТА
    ['VIETNAM, Aroti', 'горький, чернослив, темный шоколад', 2000, 'средняя', 'Вьетнам', 'робуста'],
    ['UGANDA , Aroti', 'горький, темный шоколад', 2500, 'средняя', 'Уганда', 'робуста'],
    ['Робуста Уганда BESTCOFFEE', 'темный шоколад', 250, 'средняя', 'Уганда', 'робуста'],
]

with open('coffee_dataset.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

