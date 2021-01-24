# GEEKBRAINS HOMEWORK  LESSON 3


# 1

# a = float(input("VVedi chislo #1 <<<"))
# b = float(input("VVedi chislo #2 <<<"))
#
#
# def myfunc(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "/0"
#
#
# print(myfunc(a, b))


# 2

# def heyUser(name, surname, birthYear, homeCity, email, phone):
#     return (name, surname, birthYear, homeCity, email, phone)
#
#
# user1 = heyUser(name="John", surname="Doe", birthYear="1990", homeCity="DC", email="kek@gmail.com",
#                 phone="+79999999999")
# print(*user1)  # John Doe 1990 DC kek@gmail.com +79999999999


# 3

# def my_func(a, b, c):
#     list = sorted([a, b, c])
#     #print(list)
#     return list[1] + list[2]
#
# a = my_func(100, 200, -30)
# print(a) ##300


# 4

# print("X v stepen Y. x(float)>0, y(int)<0")
# x = float(input("Vvedi X <<< "))
# y = int(input("Vvedi Y <<< "))
#
# print(x, y)
#
# def myfunc(x, y):
#     return x ** y
#
# print(myfunc(x, y))


# 5

# sum = 0
# while True:
#     stroka = input("vvedite (INT) chisla cherez probel, dlya otmeni vvedi bukvu ili oblazhaysya s probelami <<< ")
#     stroka_new = stroka.split(" ")
#     # print(stroka_new)
#     status = 0
#     for el in stroka_new:
#         try:
#             sum = sum + int(el)
#         except ValueError:
#             status = 1
#             break
#     print("Summa", sum)
#     if status == 1:
#         break

# 6


# def int_func(stroka):
#     stroka_new = stroka.split(" ")
#     # print(stroka_new)
#     for i, el in enumerate(stroka_new):
#         stroka_new[i] = el.capitalize()
#
#     return " ".join(stroka_new)
#
#
# print(int_func("bbbb"))
#
# stroka = input("Vvedi slova, razdelyai probelom <<< ")
#
# print(int_func(stroka))
