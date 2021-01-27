# GEEKBRAINS HOMEWORK  LESSON 4


# 1 Считаем зарплату. На вход кол-во часов, стоимость часа и премия, все 3 аргумента нужны

# import sys
#
# try:
#     print("workHours", sys.argv[1], "hourPrice", sys.argv[2], "bonus", sys.argv[3])
# except IndexError:
#     print("invalid args")
#     exit()
#
# print("Salary", float(sys.argv[1]) * float(sys.argv[2]) + float(sys.argv[3]))


# 2 Генерируем список и выводим значения, которые больше предыдущих

# from random import randint
#
# someList = [randint(0, 1000) for x in range(1, 100)]
# newList = []
# print(someList)
# lastItem = someList[0]
#
# for item in someList:
#     if item > lastItem:
#         newList.append(item)
#     lastItem = item
#
# print(newList)


# 3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21 в одну строку

# print([x for x in range(20, 241) if (x % 20 == 0) or (x % 21 == 0)])


# 4 Определить элементы списка, не имеющие повторений

# from random import randint
#
# someList = [randint(0, 50) for x in range(1, 50)]
# print(someList)
#
# someList2 = [x for x in someList if someList.count(x) == 1]
# print


# 5 Произвести перемножение четных чисел от 100 до 1000. Поменяйте рендж скажем до 107 и увидите, что все четко

# from functools import reduce
#
# someList = [x for x in range(100, 1001) if x % 2 == 0]
#
# print(someList)
#
#
# def my_multiple(prev_el, el):
#     return prev_el * el
#
#
# print(reduce(my_multiple, someList))


# 6-a Итератор, генерирующий целые числа, начиная с указанного. Выходит на 10ом числе

# import sys
# from itertools import count
#
# try:
#     print("Starting number", sys.argv[1])
# except IndexError:
#     print("invalid args")
#     exit()
#
#
# def myCount(startNum):
#     i = 0
#     myList = []
#     for el in count(int(startNum)):
#         if i >= 10:
#             break
#         myList.append(el)
#         i += 1
#     return myList
#
#
# print(*myCount(sys.argv[1]))  ## и вот в таком же виде будем передавать это во второй скрипт, пример 10 11 12 13 14 15 16 17 18 19


# 6-б  Итератор, повторяющий элементы некоторого списка, определенного заранее. Пример python example04.py 10 11 12 13
# Опять же не самая ясная формулировка, поэтому 2 варианта сделал
#
# import sys
# from itertools import count, cycle
#
# myList = []
#
# for el in sys.argv:
#     if el != sys.argv[0]:
#         myList.append(int(el))
#
# print("Using list ", myList)
# repeats = int(input("Enter N repeats "))
#
#
# def myRepeat1(myList, n=1):
#     iter = cycle(myList)
#     for el1 in range(0, n):
#         for el in myList:
#             print(next(iter), end=" ")
#
#
# def myRepeat2(myList, n=1):
#     iter = cycle(myList)
#     for el in myList:
#         printed = next(iter)
#         for el1 in range(0, n):
#             print(printed, end=" ")
#
#
# myRepeat1(myList, repeats)  # n=2, выведет 10 11 12 13 10 11 12 13
# print()
# myRepeat2(myList, repeats)  # n=2, выведет 10 10 11 11 12 12 13 13


# 7 Если честно, я голову сломал с прочтением этого задания, оставляю на откуп

# n = 4 # Задайте значение для n тут
#
# def fact(n):
#     result = []
#     factorial = 1
#     i = 1
#     while i <= n:
#         factorial *= i
#         result.append(factorial)
#         i += 1
#     for el in result:
#         yield el
#
#
# print(type(fact(n)))
#
# for el in fact(n):
#     print(el)
