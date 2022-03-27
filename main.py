def file_reader(): 
    cook_book = {} 
    with open('Recipies.txt', 'r', encoding='utf-8') as file: 
        for i in range(2): 
            dish_name = file.readline().strip() 
            cook_book[dish_name] = [] 
            qwnty_ingr = int(file.readline()) 
            r = [] 
            for i in range(qwnty_ingr):  
                line = file.readline().strip() 
                spl = line.split('|')
                res = {'ingredient_name': spl[0], 'quantity' : int(spl[1]), 'measure': spl[2]} 
                r.append(res)
            cook_book[dish_name] = r 
    return(cook_book) 
 
print(file_reader())

#def ingr_format():
    #for ingr in r:
        #print(ingr)
    # spl = r.split(' | ') 
    # res = {'ingredient_name': spl[0], 'quantity' : int(spl[1]), 'measure': spl[2]} 
    # return res
#print(ingr_format()) 
