'''Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам '''

song = input("Введите вашу фразу: ").lower()
list_song = song.split()
print(list_song)

def counter_vowel(word):
    counter_vowel_list=[]
    counter = 0
    vowel_letter = ["а", "е", "ё", "и", "о", "у", "э", "ы", "ю", "я"]
    for indx, value in enumerate(word):
        for i in range(len(value)):
            for j in range(len(vowel_letter)):
                if vowel_letter[j] == value[i]:
                    counter += 1
        print('Количество гласных на', indx, 'строке =',counter )
        counter_vowel_list.append(counter)
        counter = 0
    print(counter_vowel_list)
    for i in range(len(counter_vowel_list)):
        count = counter_vowel_list[0]
        if count == counter_vowel_list[i]:
            print('Парам пам-пам')
        else:
            print('Пам парам')

counter_vowel(list_song)
             