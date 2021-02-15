# GEEKBRAINS HOMEWORK  LESSON 7


# 1 Создаем матрицу, перегружаем str и add
#
# class Matrix:
#     inputValue = []
#
#     def __init__(self, inputValue):
#         self.inputValue = inputValue
#
#     def __str__(self):
#         _str = ""
#         for item in self.inputValue:
#             _str = _str + str(item) + "\n"
#         return _str
#
#     def __add__(self, other):
#         _res = []
#         _res2 = []
#
#         for j, el in enumerate(self.inputValue):
#
#             for i, el2 in enumerate(el):
#                 try:
#                     #  print(f"{el2} + {other.inputValue[j][i]} = {el2 + other.inputValue[j][i]}") отладочная строка
#                     sum = el2 + other.inputValue[j][i]
#                     _res2.append(sum)
#                 except IndexError:
#                     pass
#
#             _res.insert(j, _res2.copy())
#             _res2.clear()
#
#         self.inputValue = _res
#         return self
#
#
# a = Matrix([[1, 2, 3], [2, 3, 4], [6, 0, 1]])
# b = Matrix([[6, 9, 31], [2, 5, 4], [1]])
#
# print(a)
# print(b)
# c = a + b
# print(c)
# print(type(c))


# 2

# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     name: str
#
#     def __init__(self, name: str):
#         self.name = name
#
#     @abstractmethod
#     def calc_cloth(self):
#         pass
#
#     @abstractmethod
#     def name_size(self):
#         pass
#
#
# class Palto(Clothes):
#     size: float
#
#     def __init__(self, size: float, name: str):
#         self.size = size
#         Clothes.__init__(self, name)
#
#     def calc_cloth(self):
#         # return self.size / 6.5 + 0.5
#         return f"{(self.size / 6.5 + 0.5):.2f}"
#
#     @property
#     def name_size(self):
#         return f"{self.name} {self.size}"
#
#
# class Kostum(Clothes):
#     height: float
#
#     def __init__(self, height: float, name: str):
#         self.height = height
#         Clothes.__init__(self, name)
#
#     def calc_cloth(self):
#         return f"{(self.height * 2 + 0.3):.2f}"
#
#     @property
#     def name_size(self):
#         return f"{self.name} {self.height}"
#
#
# class Compose(Clothes):
#     def __init__(self, children: list):
#         self.children = children
#
#     def calc_cloth(self):
#         for item in self.children:
#             print(item.calc_cloth())
#
#     def name_size(self):
#         for item in self.children:
#             print(item.name_size())
#
#     def calc_summary(self):
#         summ = 0
#         for item in self.children:
#             summ = summ+ float(item.calc_cloth())
#         return summ
#
#
# a = Kostum(100, "kostum1")
# b = Palto(33, "palto1")
#
# print(a)
# print(b)
# print(a.calc_cloth())
# print(b.calc_cloth())
#
# print(a.name_size)
# print(b.name_size)
#
# c = Compose([a, b])
# c.calc_cloth()
#
# print(f"Summary {c.calc_summary():.2f}")


# 3

# class Cell():
#     c_count: int
#
#     def __init__(self, count: int = 1):
#         self.c_count = count
#
#     def __add__(self, other):
#         new = self.c_count + other.c_count
#         print(f"cell({self.c_count}) + cell({other.c_count}) = cell({new})")
#         self.c_count = new
#         return self
#
#     def __sub__(self, other):
#         if self.c_count - other.c_count > 0:
#             new = self.c_count - other.c_count
#             print(f"cell({self.c_count}) - cell({other.c_count}) = cell({new})")
#             self.c_count = new
#             return self
#         else:
#             print("CANNOT MINUS LESS THAN 0")
#             raise NotImplementedError
#
#     def __mul__(self, other):
#         new = self.c_count * other.c_count
#         print(f"cell({self.c_count}) * cell({other.c_count}) = cell({new})")
#         self.c_count = new
#         return self
#
#     def __truediv__(self, other):
#         new = self.c_count // other.c_count
#         print(f"cell({self.c_count}) // cell({other.c_count}) = cell({new})")
#         self.c_count = new
#         return self
#
#     def make_order(self, n: int):
#         new = self.c_count % n
#         new2 = self.c_count // n
#         print("new =", new, "new2 =", new2, "c.count =", self.c_count)
#         i = 0
#         res = ""
#         while (i < new2):
#             res = res + ("*" * n) + "\n"
#             i += 1
#         res = res + ("*" * new) + "\n"
#         print(res)
#
#
# a = Cell(5)
# b = Cell(4)
# c = Cell(10)
#
# a + b
# b + c
# try:
#     f = a - c
# except NotImplementedError:
#     pass
#
# f = a * c
# a * b
# a / c
#
# print("#####")
# print(a.c_count)
# print(b.c_count)
# print(c.c_count)
# print(f.c_count)
# print("#####")
# print("a")
#
# d = Cell(50)
# c.make_order(4)
#
# d.make_order(4)
#
# f = Cell(15)
# f.make_order(5)
