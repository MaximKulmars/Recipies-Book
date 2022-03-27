def file_opener():
    with open('Recipies.txt', 'r', encoding='utf-8') as file: # открыли файл
        cook_book = {} # создаём пустой словарь
        dish_name = file.readline() # читаем строку с названием блюда и потом кладём его в словарь как ключ (строка 5)
        cook_book[dish_name] = [] 
        qwnty_ingr = int(file.readline()) # считываем количество итераций для цикла ниже
        for i in range(qwnty_ingr):
           d = {i.split("|")[0]: " ".join(i.replace("\n", "").split(" ")[1:]) for i in file}
           print(d)
print(file_opener())