list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


list_2 = [] # новый список который будет собирать
for i in list_1:
    if i.isdigit(): # Проверка стриновых строк на  присутвие  чисел
        list_2.extend(['"',f'{int(i):02}','"']) # extend - добавляет елементы оптом, :02 - добавление нулей
    elif (i.startswith('+')) or (i.startswith('-')) and i[1:].isdigit(): # startswith - проверка на первый элемент
        list_2.extend(['"',f'{i[0]}{int(i[1:]):2}','"'])
    else:
        list_2.append(i)
out_list_2 = ' '.join(list_2) # методом join раставляю проблемы 
print(out_list_2)