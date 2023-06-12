#
# class Car:
#
#     def __init__(self, wheels, brand, price, year):
#         self.wheels = wheels
#         self.brand  = brand
#         self.price = price
#         self.year = year
#     def __eq__(self, other):
#         if isinstance(other, Car):
#             return self.wheels == other.wheels
#         if isinstance(other, int):
#             return self.wheels == other
#     def __lt__(self, other):
#         if isinstance(other, Car):
#             return self.year < other.year
#         if isinstance(other, int):
#             return self.year < other
#
#     def __gt__(self, other):
#         if isinstance(other, Car):
#             return self.price > other.price
#         if isinstance(other, int):
#             return self.price > other
#
#     def __add__(self, other):
#         if isinstance(other, Car):
#             return self.price + other.price
#         if isinstance(other, int):
#             return self.price + other
#     def __sub__(self, other):
#         if isinstance(other, Car):
#             return self.price - other.price
#         if isinstance(other, int):
#             return self.price - other
#     def __mul__(self, other):
#         if isinstance(other, Car):
#             return self.year * other.year
#         if isinstance(other, int):
#             return self.year * other
#     def __truediv__(self, other):
#         if isinstance(other, Car):
#             return self.year / other.year
#         if isinstance(other, int):
#             return self.year / other
# a1 = Car(4,"Sifsi", 2500, 2003, )
# a2 = Car(4,"Sifsi", 3500, 2001, )
#
# print(a1 == a2)
# print(a1 < a2)
# print(a1 > a2)
# print(a1 * a2)
# print(a1 - a2)

# class  Student:
#     def __init__(self, name, school, marks):
#         self.name = name
#         self.school = school
#         self. marks = list(marks)
#
#     def add_marks(self, item):
#         self.marks.append(item)
#
#     def getitem(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError('Неверный идекс')
#
#     def setitem(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым неотрицательным числом')
#
#         self.marks[key] = value
#
#     def delitem(self, key):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым неотрицательным числом')
#
#         del self.marks[key]
#
#     def get_average(self):
#         return sum(self.marks)//len(self.marks)
# a1 = Student("Agahan", 63, [3, 4, 5, 5, 4])
# a2 = Student("Kutman", 72, [4, 5, 5, 5, 3, 4, 5, 5])
# a2.marks[3] = 15
# a2.add_marks(25)
# print(a2.marks)
# print(a2.get_average())





