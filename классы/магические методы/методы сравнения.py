# class Vector:
#     def __init__(self, x):
#         self.x = x
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return self.x + other.x
#         if isinstance(other, int):
#             return self.x + other
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return self.x - other.x
#         if isinstance(other, int):
#             return self.x - other
#
#
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             return self.x * other.x
#         if isinstance(other, int):
#                 return self.x * other
#
#     def __truediv__(self, other):
#         if isinstance(other, Vector):
#             return self.x / other.x
#         if isinstance(other, int):
#                 return self.x / other
#
# a1 = Vector(30)
# a2 = Vector(20)
#
# print(a1 + a2)
# print(a1 + 100)
# print(a1-a2)
# print(a1 * a2)
# print(a1 / a2)


class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute


    def __eq__(self, other):
        if not isinstance(other, Time):
            raise TypeError("aidai")

        if self.hour == other.hour and self.minute == other.minute:
           return True
        else:
           return False

    def __lt__(self, other):
        if not isinstance(other, Time):
            TypeError("aidai")

        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False


a1 = Time(6, 20)
a2 = Time(6, 30)

print(a1 == a2)
print(a1 < a2)
print(a1 > a2)

