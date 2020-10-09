# Сздать N-e количество списков на 8 эллементов кратных 5 и сумма которых даст 100 
# 
# Пример:
# [5, 10, 15, 20, 15, 15, 10, 10]

import random

def start():
    setHundreds = []
    randHundreds = []
    for i in range(5,35,5):                                         # Создаём массив от 5 до 35 с шагом 5  
        setHundreds.append(i)
        randHundreds.append(random.choice(setHundreds))             # Рандомно выбрав эллементы записываем в другой список

    finalyHundreds = 100 - sum(randHundreds)                        # Смотрим сколько осталось 

    if finalyHundreds % 2 == 0 :                                    # Проверяем на четность остаток, что бы дописать 7 и 8 эллемент
        seventhVariable = int(finalyHundreds / 2)
        eighthVariable = seventhVariable
        randHundreds.append(seventhVariable)
        randHundreds.append(eighthVariable)
    else:
        randHundreds.append(finalyHundreds-5)
        randHundreds.append(5)
    
    return print(randHundreds)

if __name__ == '__main__':
    counter = 0
    while counter != 100:
        start()
        counter += 1