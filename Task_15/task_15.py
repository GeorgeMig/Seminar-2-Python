#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел. 


def sequence(num):
    list = []
    i = num * -1
    while i <= num:
        list.append(i)
        i += 1
    return list

def find_position(list):
    position = input('Введите позиции искомых элементов через пробел: ')
    print(f'Произведение элементов на указанных позициях = {list[int(position[0])] * list[int(position[2])]}')
    
n = 4
my_list = sequence(n)
print(my_list)
find_position(my_list)