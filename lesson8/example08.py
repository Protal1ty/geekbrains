# GEEKBRAINS HOMEWORK  LESSON 8


# 1

# class Data:
#     data: str
#     day: int
#     month: int
#     year: int
#
#     def __init__(self, data: str):
#         self.data = data
#
#     @classmethod
#     def daymonyear(cls, arg: str, ret: str):  ## ret - собственно выбор что вернуть
#         if cls.checkinput(arg) == False:
#             return False
#
#         inp_split = arg.split("-")
#         day = int(inp_split[0])
#         mon = int(inp_split[1])
#         year = int(inp_split[2])
#         if ret == "d":
#             return day
#         if ret == "m":
#             return mon
#         if ret == "y":
#             return year
#
#     @staticmethod
#     def checkinput(inp: str):
#         inp_split = inp.split("-")
#         print(inp_split)
#         try:
#             day = int(inp_split[0])
#             mon = int(inp_split[1])
#             year = int(inp_split[2])
#         except ValueError:
#             print("Invalid input")
#         if day // 31 >= 1 or day <= 0:  ##Хотя глобально проверять на отрицательное число не нужно, парсится все по -, а ввод строго задан в задании
#             print("Invalid day input")
#             return False
#         if mon // 13 >= 1 or mon <= 0:
#             print("Invalid month input")
#             return False
#
#         print("All is good")
#         return True
#
#
# a = Data("10-14-2021")
# print(Data.checkinput("01-12-2021"))
# Data.daymonyear("10-14-2021", "d")  # d или m или y
# print(Data.daymonyear("10-09-2021", "m"))
#

# 2
#
# class Zerodiv(Exception):
#     def __init__(self, arg1, arg2):
#         print(f"DIVISION BY ZERO EXCEPTION, CANT DIVIDE {arg1} BY {arg2}")
#
#
# def dividepls(a, b):
#     if b == 0:
#         raise Zerodiv(arg1=a, arg2=b)
#     return a / b
#
# try:
#     print(dividepls(100, 500))
#     print(dividepls(100, 0))
# except Zerodiv:
#     print("DONT DO THIS")

# 3

# class ContainsLetter(Exception):
#     def __init__(self):
#         print("CONTAINS LETTERS")
#
#
# def checkInp(arg):
#     try:
#         int(arg)  # Сказали, что только числа и строки, а значит в данном примере вполне допустимо
#     except ValueError:
#         raise ContainsLetter
#     print(arg)
#
#
# spisok = []
#
# while True:
#     try:
#         inElement = input("Vvedi element, 'stop'- konec <<< ")
#         if inElement == "stop":
#             break
#         checkInp(inElement)
#         spisok.append(inElement)
#     except ContainsLetter:
#         print("Dont input letters")
#
#     print(spisok)
#
# print("Vash spisok >>> ", spisok)
# spisokLen = len(spisok)
# print("Kolvo elementov", spisokLen)


# 4-6

# class WareHouse:
#     items: dict
#
#     # count: int
#
#     def __init__(self):
#         self.items = {}
#
#     def checkInt(self, var):
#         if (isinstance(var, int)):
#             pass
#         else:
#             raise ValueError
#
#     def putIn(self, arg, count=1):
#         # arg.type, arg.model
#         self.checkInt(count)
#         try:
#             if self.items[f"{arg.type} {arg.model}"]:
#                 somevar = self.items[f"{arg.type} {arg.model}"]
#                 self.items[f"{arg.type} {arg.model}"] += count
#                 print(f"Put {arg.type} {arg.model} {somevar}")
#         except KeyError:
#             self.items[f"{arg.type} {arg.model}"] = count
#             print(f"Put {arg.type} {arg.model} {count}")
#             print("Warehouse has", self.items)
#
#     def getItem(self, arg, department="none", count=1):
#         self.checkInt(count)
#         if department == "none":
#             somevar = self.items[f"{arg.type} {arg.model}"] - count
#             if somevar < 0:
#                 print("Cannot allocate items, not enough in warehouse")
#                 return 0
#             else:
#                 self.items[f"{arg.type} {arg.model}"] = somevar
#                 print(f"Get {arg.type} {arg.model} {count}")
#             #  print(self.items)
#             #  print(self.items[f"{arg.type} {arg.model}"])
#             #   department.putIn(f"{arg.type} {arg.model}", count)
#
#             #    print(self.items[f"{arg.type} {arg.model}"])
#             print("LEFT", self.items)
#         else:
#             somevar = self.items[f"{arg.type} {arg.model}"] - count
#             if somevar < 0:
#                 print("Cannot allocate items, not enough in warehouse")
#                 return 0
#             else:
#                 self.items[f"{arg.type} {arg.model}"] = somevar
#                 print(f"Get {arg.type} {arg.model} {count}")
#                 print("LEFT", self.items)
#                 department.putIn(f"{arg.type} {arg.model}", count)
#         # self.items.extend(arg)
#
#
# class Department:
#     items: dict
#     name: str
#
#     def checkInt(self, var):
#         if (isinstance(var, int)):
#             pass
#         else:
#             raise ValueError
#
#     def __init__(self, name):
#         self.name = name
#         self.items = {}
#
#     def putIn(self, arg, count: int):
#         self.checkInt(count)
#         try:
#             if self.items[arg]:
#                 somevar = self.items[arg]
#                 self.items[arg] += count
#                 print(f"Put in Department {self.name} {arg} {somevar}")
#         except KeyError:
#             self.items[f"{arg}"] = count
#             print(f"Put in Department {self.name} {arg} {count}")
#             print(f"Department {self.name} has {self.items}")
#
#
# class OrgTech:
#     type: str
#     model: str
#
#     def __init__(self, type: str, model: str):
#         self.type = type
#         self.model = model
#
#
# class Printer(OrgTech):
#     def __init__(self, model):
#         super().__init__("printer", model)
#
#
# class Scanner(OrgTech):
#     def __init__(self, model):
#         super().__init__("scanner", model)
#
#
# class Xerox(OrgTech):
#     def __init__(self, model):
#         super().__init__("xerox", model)
#
#
# b = WareHouse()
# a = Printer("AX90")
# d = Department("SomeDep")
#
# # print(a)
# # print(a.model)
# # print(a.type)
#
# b.putIn(a)
# # print(b.items)
#
# c = Printer("DX230")
# b.putIn(c, 20)
# b.putIn(c, 21)
# b.getItem(c, d, count=10)
# b.getItem(a, d)
# # b.getItem(a, d)
# print(d.items)
# # print(b.items)


# 7

# class ComplexN:
#     # a + b*i
#     # Делаем допущение, что мы НЕ меняем переменные в процессе подсчетов, те при a+b, а не меняется в итоге, мы создаем новую переменную в итоге рассчетов
#     a = float
#     b = float
#     i = "j"
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         if self.b > 0:
#             return f"{self.a} + {self.b}j"
#         if self.b < 0:
#             return f"{self.a} - {self.b}j"
#         if self.b == 0:
#             return f"{self.a}"
#
#     def __add__(self, other):
#         a = self.a + other.a
#         b = self.b + other.b
#         res = ComplexN(a, b)
#         print("summ =", res)
#         return res
#
#     def __mul__(self, other):
#         a = self.a * other.a - self.b * other.b
#         b = self.a * other.b + self.b * other.a
#         res = ComplexN(a, b)
#         print("mult =", res)
#         return res
#
#
# a = ComplexN(10, 90)
# b = ComplexN(5, 40)
#
# a
# print("a:", a)
# print("b:", b)
#
# c = a + b
# print("c:", c)
# print("a:", a)
# print("b:", b)
# a * b
