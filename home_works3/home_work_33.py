'''
Задание №3
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''

text = ("Для человека просто невозможно представить действительные размеры Вселенной. \
        Мы не только не знаем, насколько она велика, но нам даже трудно вообразить,  \
        насколько она может простираться.  \
        Если мы начнем удаляться от Земли, мы поймем, почему это так. Земля — это маленькая частичка  \
        Солнечной системы. В Солнечную систему входят Солнце, планеты, которые вращаются вокруг Солнца, \
        астероиды, представляющие собой маленькие планеты, и метеоры.\
        Вся наша Солнечная система в свою очередь является небольшой частью другой большой системы, \
        называемой «галактика». Галактика состоит из миллионов и миллионов звезд, многие из которых \
        значительно больше нашего Солнца и имеют свои солнечные системы.\
        Итак, все звезды которые мы наблюдаем в нашей галактике и которую мы называем «Млечный Путь»,\
        являются «солнцами». Расстояние между ними измеряется в световых годах, а не в километрах.\
        За один год луч света проходит более 11 000 000 000 000 км. Альфа Центавра — самая близкая и\
        яркая звезда — расположена на расстоянии более 46 000 000 000 000 км от нас.\
        Но давай представим размеры нашей галактики. Считается, что ее диаметр достигает 100 000 световых\
        лет. Это означает 100 000 раз по 11 000 000 000 000 км. Но наша галактика в свою очередь является \
        малой частью другой, более крупной системы.")

delite_chars = ".,!?,;:'=÷×+-"
text = text[::-1]
for i in text:
    for j in delite_chars:
        text = text.replace(j, "")

text = text.lower().split(" ")

counter_word = []
for i in range(len(text)):
    count = 0
    for j in text:
        if text[i] == j:
            count += 1
    counter_word.append(str(count) + " - " + text[i][::-1])

counter_word = set(counter_word)
counter_word = sorted(counter_word)[::-1]
counter_word = counter_word[:10:]
print(counter_word)