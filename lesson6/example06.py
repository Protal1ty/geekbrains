# GEEKBRAINS HOMEWORK  LESSON 6


# 1 Создаем светофор с методом переключания цвета. Каждый цвет держится н секунд. красный, желтый, зеленый - строго по очереди

# import time
#
#
# class TrafficLight:
#     color = ""
#     counter = 0 ## Вроде запрета на доп переменных не было
#
#     def running(self, inColor=None):
#         __cycle = ("red", "yellow", "green")
#         __cycleDict = {"red": 5, "yellow": 2, "green": 7}
#         if inColor == None:  ##просто автоматом переключает цвета и выводит
#             self.color = "red"
#             print(self.color)
#             time.sleep(5)
#             self.color = "yellow"
#             print(self.color)
#             time.sleep(2)
#             self.color = "green"
#             print(self.color)
#             time.sleep(7)
#         if inColor != None:
#             try:
#                 __res = __cycle.index(inColor)
#                 if self.counter != __res:
#                     print("Wrong order")
#                     exit(0)
#                 else:
#                     self.color = __cycle[__res]
#                     print(self.color)
#                     time.sleep(__cycleDict.get(self.color))
#                     self.counter += 1
#                     self.counter = self.counter%3
#
#             except ValueError:
#                 print("Does not exist in Traffic light")
#
#
# a = TrafficLight()
# #a.running()
# a.running("red")
# a.running("yellow")
# a.running("green")
# a.running("green") ## даст ошибку, тк не по порядку меняем цвет
# a.running("green") ## уже не выполнится - выход был


# 2 Создаем класс дороги с защищенными длиной\шириной, создаем метод подсчета массы асфальта, нужного для этой дороги

# class Road:
#
#     def __init__(self, len, wid):
#         self._length = len
#         self._width = wid
#
#     def calc(self, mas=25, height=1):
#         __res = self._length * self._width * mas * height
#         print("Needed", __res, "kg")
#
#
# a = Road(100, 200)
# a.calc()
# a.calc(40, 10)


# 3 Делаем класс worker с некоторыми параметрами, последний защищенный, после наследуем его в position и делаем методы для вывода имени\полного заработка


# class Worker:
#
#     def __init__(self, inName, inSurname, inPosition, inWage, inBonus):
#         self.name = inName
#         self.surname = inSurname
#         self.position = inPosition
#         self._income = {"wage": inWage, "bonus": inBonus}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return (f"{self.name} {self.surname}")
#
#     def get_total_income(self):
#         return (sum(self._income.values()))
#
#
# a = Position("NotJohn", "NotDoe", "NotManager", 90000, 100000)
# b = Position("John", "Doe", "Manager", 50000, 20000)
# print(b.name)
# print(b.surname)
# print(b.position)
# print(b.get_full_name())
# print(b.get_total_income())
#
# print(a.name)
# print(a.surname)
# print(a.position)
# print(a.get_full_name())
# print(a.get_total_income())


# 4-5 Делаем класс car, наследуемся, переопределяем метод, делаем экземпляры классов, обращаемся ко всему внутри

#
# class Car:
#     def __init__(self, inColor, inName, inSpeed=0, inPolice=False):
#         self.speed = inSpeed
#         self.color = inColor
#         self.name = inName
#         self.is_police = inPolice
#
#     def go(self, inSpeed):
#         print(f"{self.name} goes brrr {inSpeed} km/h")
#         self.speed = inSpeed
#         return (self.speed)
#
#     def stop(self):
#         print(f"{self.name} stops")
#         self.speed = 0
#         return (self.speed)
#
#     def turn(self, direction):
#         print(f"{self.name} turns {direction}")
#         self.direction = direction
#         return (self.direction)
#
#     def show_speed(self):
#         print(f"{self.name} speed is {self.speed} km/h")
#         return (self.speed)
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60:
#             print(f"{self.name} speed is too high!! {self.speed} km/h")
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed > 40:
#             print(f"{self.name} speed is too high!! {self.speed} km/h")
#
#
# class PoliceCar(Car):  ## Формально класс есть, описывать что-то дополнительное в него не вижу смысла
#     pass
#
#
# class SportCar(Car):
#     pass
#
#
# tc1 = TownCar("White", "TownCar1")
# wc1 = WorkCar("Black", "WorkCar1")
# pc1 = PoliceCar("Blue", "PoliceCar1", inPolice=True)
# sp1 = SportCar("Red", "SportCar1")
#
# tc1.go(40)
# wc1.go(50)
# pc1.go(60)
# sp1.go(190)
#
# tc1.show_speed()
# wc1.show_speed()
# pc1.show_speed()
# sp1.show_speed()
#
# tc1.stop()
# tc1.turn("somewhere")
# tc1.go(60)
# tc1.show_speed()
#
# print(type(pc1.is_police))
# print(pc1.is_police)
# print(pc1.speed)
# print(pc1.color)
# print(pc1.name)


# 6 Делаем класс, переопределяем метод draw во всех наследниках, делаем экземляры, смотрим результат

class Stationery:
    def __init__(self, inTitle):
        self.title = inTitle

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(self.title + " " + "Рисуем ручкой")


class Pencil(Stationery):
    def draw(self):
        print(self.title + " " + "Рисуем карандашом")


class Handle(Stationery):
    def draw(self):
        print(self.title + " " + "Рисуем маркером")


a = Pen("Erich Krause")
b = Pencil("No name")
c = Handle("Stabilo")
a.draw()
b.draw()
c.draw()
a.draw()
c.draw()
