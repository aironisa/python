class Vehicle:
    def __init__(self, max_speed, num_wheels):
        self.max_speed = max_speed
        self.num_wheels = num_wheels


# class Car(Vehicle):
#     def __init__(self, max_speed, num_wheels, brend):
#         super().__init__(max_speed, num_wheels )
#         self.brend = brend
#
#     def qet_info(self):
#         print(f'max_speed {self.max_speed}, num_wheels {self.num_wheels}, brend {self.brend}')
#
#
# class Motocycle(Vehicle):
#     def __init__(self, max_speed, num_wheels, mark):
#         super().__init__(max_speed, num_wheels)
#         self.mark = mark
#
#     def qet_info(self):
#         print(f'max_speed {self.max_speed}, num_wheels {self.num_wheels}, brend {self.mark}')
#
# a = Car (150, 4, "lexus")
# a.qet_info()
# b = Motocycle(140, 2, "aikoo" )
# b.qet_info()



# class Libary:
#     def __init__(self, books):
#         self.__books = books
#
#     def add_book(self, name):
#
#         self.__books.append(name)
#
#     def delete_book(self, name):
#         self.__books.remove(name)
#
#     def qet_books(self):
#         print(self.__books)
#
# a = Libary(["Магия утро"])
# a.add_book("богатый папа")
# a.delete_book("Магия утро")
# a.qet_books()



class Car:
    def get_info(self):
        pass

class BMW(Car):
    def __init__(self, model, max_speed, num_wheels):
        self.model = model
        self.max_speed = max_speed
        self.num_wheels = num_wheels
    def get_info(self):
        print(f'model {self.model}, max_speed {self.max_speed}, num_wheels {self.num_wheels}')

class Mercedes(Car):

    def __init__(self, num_seat, engine, model):
        self.num_seat = num_seat
        self.engine = engine
        self.model = model
    def qet_info(self):
        print(f'num_seat {self.num_seat}, engine {self.engine}, model {self.model}')

class Subaru(Car):
    def __init__(self, num_window, price, model ):
        self.num_window = num_window
        self.price = price
        self.model= model
    def qet_info(self):
        print(f'num_window {self.num_window}, price {self.model}, model {self.price}')

a = BMW("BMW x6", 150, 4)
a.get_info()
a = Mercedes(8, 60, "Mersedes Benz")
a.get_info()
a = Subaru(4, 200, "Subaru XV")
a.get_info()