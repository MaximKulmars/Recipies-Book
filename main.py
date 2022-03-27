  
def dict_creator():
    with open('Recipies.txt', 'r', encoding='utf-8') as file: # открывает файл
        cook_book = {} # создаём пустой словарь
        dish_name = file.readline() # читаем название блюда из первой строки
        cook_book[dish_name] = [] # создаём ключ с названием блюда
        qwnty_ingr = int(file.readline()) # считываем количество ингризиентов, которое будет использовано для количесва итераций в цикле ниже
        for i in range(qwnty_ingr): 
           line = file.readline() # построчно считываем ингридиенты
           splited_line = line.split('|') # разбиваем строку и преобразуем в список
           print(splited_line)
        #    cook_book[dish_name].append(format_ingr(splited_line))
        # return(cook_book)
print(dict_creator())