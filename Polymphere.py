# # Len used in number of charcter
# # x = "Hello Parash Thami"
# # print(len(x))
#
# # Tuple len() return the number  of items in the tuple:
#
# # mytuple = ("Apple", "Banana", "Cherry", "Grapes")
# # print(len(mytuple))
#
# # Dictionaries len() returns the number of Key/value pairs in the dic
# # thisdict = {
# #     "brand": "Ford",
# #     "model": "Mustang",
# #     "year": 1689
# # }
# # print(len(thisdict))
# import self as self


# Class polymphere
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        def move(self):
            print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
 x.move()
