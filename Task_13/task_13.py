# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. 

def fact_num(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    print(res, end= ' ')

num = int(input('Введите любое целое число: '))
i = 1
while i <= num:
    fact_num(i)
    i += 1

