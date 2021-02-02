# GEEKBRAINS HOMEWORK  LESSON 4


# 1 Записываем построчно в текстовый файл, выход при пустой строке. Файл создастся сам, запишется на пустой строке, формально запишется построчно
# Выбери один из двух вариантов

# print("Hello user")
# usInput = "smt"

# ################# V1 Этот блок если хотим записать файл только после пустой строки
# try:
#     with open("task1.txt", "a") as my_file:
#         while usInput != "":
#             usInput = input("Enter smt, exit with blank <<< ")
#             print(usInput, file=my_file)
#
# except IOError:
#     print("some err")
# #################

# ################# V2 Этот блок если прям хотим каждую строку введенную сразу видеть
# while usInput != "":
#     my_file = open("task1.txt", "a")
#     usInput = input("Enter smt, exit with blank <<< ")
#     print(usInput, file=my_file)
#     my_file.close()
# #################


# 2 Посчитаем колво строк и колво символов в каждой строке в файле task2.txt

# print("Hello user")
# i = 0
# lineCount = 0
# try:
#     with open("task2.txt") as my_file:
#         for line in my_file.readlines():
#             line = line.replace("\n", "")
#             print(line)
#             i += 1
#             lineCount += len(line)
#             print("Words in this line:", len(line))
#         print("Line count: ", i)
#         print("Total words: ", lineCount)
# except IOError:
#     print("some err")


# 3 Из файла task3.txt считаем фамилии и оклад, выводим людей с окладом менее 20 тыс, считаем среднюю ЗП всех

# salaryBelow = 20000
# salarySum = 0
# manCount = 0
# try:
#     with open("task3.txt") as my_file:
#         for line in my_file.readlines():
#             line = line.replace("\n", "")
#             mas = line.split(" ")
#             mas[1] = float(mas[1])
#             if mas[1] < salaryBelow:
#                 print("This man has low salary >>> ", mas[0], mas[1])
#             salarySum += mas[1]
#             manCount += 1
#         print("Average salary >>> ", salarySum / manCount)
# except IOError:
#     print("some err")


# 4 Открываем файл task4.txt, построчно переводим его и записываем в task4_result.txt

# import os
#
# def myfunc(somestring):
#     myDict = {"One": "Один",
#               "Two": "Два",
#               "Three": "Три",
#               "Four": "Четыре"}
#     return myDict.get(somestring, "ERROR")
#
# if os.path.exists("task4_result.txt"):
#     os.remove("task4_result.txt")
#
# try:
#     with open("task4.txt") as my_file:
#         for line in my_file.readlines():
#             line = line.replace("\n", "")
#             mas = line.split(" ")
#             mas[0] = myfunc(mas[0])
#             my_file = open("task4_result.txt", "a")
#             print(*mas, file=my_file)
#             my_file.close()
# except IOError:
#     print("some err")


# 5 Создаем файл (task5.txt), в нем набор чисел через пробел, считаем их сумму и выводим на экран. Не сказано, что это делает пользователь, поэтому сгенерируем

# from random import randint
#
# someList = [randint(0, 1000) for x in range(1, randint(5, 20))]
#
# print(someList)
# print("Testing only length is >>>", len(someList))
# print("Testing only sum is >>>", sum(someList))
# try:
#     with open("task5.txt", "w") as my_file:
#         print(*someList, file=my_file)
# except IOError:
#     print("some err")
#
# mySum = 0
#
# try:
#     with open("task5.txt") as my_file:
#         line = my_file.read()
#         line = line.replace("\n", "")
#         mas = line.split(" ")
#         print(mas)
#         for el in mas:
#             mySum += int(el)
#         print("SUMM IS >>>", mySum)
# except IOError:
#     print("some err")


# 6 Парсим строки вида Предмет: нЛекций(л) нПрактика(пр) нЛаборораторных(лаб) в словарь с суммой часов по каждому предметов
# Наверное множество .replace можно как-то аккуратнее сделать

# def lineClean(someString):
#     someString = someString.replace("\n", "")
#     someString = someString.replace(":", "")
#     someString = someString.replace("-", "0")
#     someString = someString.replace("(пр)", "")
#     someString = someString.replace("(лаб)", "")
#     someString = someString.replace("(л)", "")
#     return someString
#
#
# def someSum(someString):
#     return sum([int(i) for i in someString])
#
#
# try:
#     with open("task6.txt") as my_file:
#         finalDict = {}
#         for line in my_file.readlines():
#             line = lineClean(line)
#             mas = line.split(" ")
#             mySum = someSum(mas[1:])
#             finalDict[mas[0]] = mySum
#
#     print(finalDict)
#
# except IOError:
#     print("some err")


# 7 Создаем файл со строками вида firm_1 ООО 10000 5000, считаем прибыль, если компания убыточна - включаем в список, но не в общую среднюю прибыль, результат пишем в файл в task7_res.json

# import json
#
#
# def lineClean(someString):
#     someString = someString.replace("\n", "")
#     someString = someString.replace(":", "")
#     someString = someString.replace("-", "0")
#     someString = someString.replace("(пр)", "")
#     someString = someString.replace("(лаб)", "")
#     someString = someString.replace("(л)", "")
#     return someString
#
#
# def someSum(someString):
#     return sum([int(i) for i in someString])
#
#
# finalList = []
#
# try:
#     with open("task7.txt") as my_file:
#         finalDict1 = {}
#         finalDict2 = {}
#         companyCount = 0
#         totalIncome = 0
#         for line in my_file.readlines():
#             line = lineClean(line)
#             mas = line.split(" ")
#             income = int(mas[2]) - int(mas[3])
#             finalDict1[mas[0]] = income
#             if income > 0:
#                 totalIncome += income
#                 companyCount += 1
#
#         finalDict2["average_profit"] = round(totalIncome / companyCount, 2)
#         finalList.append(finalDict1)
#         finalList.append(finalDict2)
#         print(finalList)
# except IOError:
#     print("some err")
#
# with open("task7_res.json", "w") as file_stream:
#     json.dump(finalList, file_stream)
