# GEEKBRAINS HOMEWORK  LESSON 2


# 1

# spisok = [2, "abc", "dac", 9999999999999999999, 44.4, None, True]
# for el in spisok:
#     print(type(el))


# 2

# print("Zapolni spisok")
# spisok = []
#
# while True:
#     inElement = input("Vvedi element, pustoe znachenie - konec <<< ")
#     if inElement == "":
#         break
#     spisok.append(inElement)
#     print(spisok)
#
# print("Vash spisok >>> ", spisok)
# spisokLen = len(spisok)
# print("Kolvo elementov", spisokLen)
#
# i = 0
# if (spisokLen % 2 == 0):
#     while i <= spisokLen - 2:
#         spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
#         i = i + 2
#
# print("Finalniy spisok >>> ", spisok)


# 3

# my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень",
#            10: "Осень", 11: "Осень", 12: "Зима"}
# my_list = ["Зима", "Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень", "Осень"]
#
# myInp = int(input("Vvedi ot 1 do 12 <<< "))
# dict_value = my_dict.get(myInp)
# list_value = my_list[myInp - 1]
#
# print("DICT ", dict_value)
# print("LIST ", dict_value)


# 4

# stroka = input("vvedite stroku s probelami <<< ")
# stroka_new = stroka.split(" ")
#
#
# for el in stroka_new:
#     print (el[:10])
# # print(*stroka_new, sep='\n', end='\n') - полюбас как-то можно транкнуть выходящую строку тут, подскажите как


# 5

# rating = [7, 5, 3, 3, 2]
# usInput = input("Vvedi noviy rating <<< ")
#
# newRate = rating[::-1]
# try:
#     newPos1 = newRate.index(int(usInput))
#     newPos2 = len(rating) - newPos1
#     rating = rating[:newPos2] + [usInput] + rating[
#                                             newPos2:]  # не перевожу usInput в int для наглядности куда кладется новый рейт
# except ValueError:
#     rating.append(int(usInput))
#
# print(rating)

