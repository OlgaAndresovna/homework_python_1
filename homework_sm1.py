# задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input('Введите целое число '))
# sum = 0
# while number != 0:
#     sum = sum + number % 10
#     number = number // 10
# print(f'Сумма цифр введенного числа равна {sum}')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали большое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# s = int(input('Введите общее количество журавликов '))
# if s % 6 == 0:
#     print(f'Петя сделал {s//6} журавликов')
#     print(f'Катя сделала {s//3*2} журавликов')
#     print(f'Сережа сделал {s//6} журавликов')
# else:
#     print('Пересчитайте общее количество журавликов')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# n = list(input('Введите число '))
# if len(n) != 6:
#   print('Check that the input is correct')
# else:
#   s1 = int(n[0]) + int(n[1]) + int(n[2])
#   s2 = int(n[3]) + int(n[4]) + int(n[5])
#   if s1 == s2:
#     print('yes')
#   else:
#     print('no')
