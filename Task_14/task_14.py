#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

def sequence(num):
    list = []
    i = 1
    while i <= num:
        list.append((1+1/i) ** i)
        i += 1
    return list

def sum_sequences(list):
    res = 0
    for i in list:
        res += i
    print(f'Сумма элементов последовательности = {res}')
    
n = 4
my_list = sequence(n)
print(my_list)
sum_sequences(my_list)

