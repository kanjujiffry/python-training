from datetime import datetime


class car:
    def __init__(self, brandname, year, origin="AMERICA"):
        self.brand = brandname
        self.year = year
        self.orgin = origin
# Regular  method

    def stats(self):
        print("this is {}, it is made in {} in {}".format(self.brand, self.origin, self.year))

    def just_fun(self):
        self.forfun = self.self.brand + "is stupid"
        return self.forfun

    @classmethod
    def setting(cls, number):
        cls.number_of_wheels = number

    @classmethod
    def alternative_init(cls, string):
        brand, year, origin = string.split("-")
        return cls(brand, year, origin)

    @staticmethod
    def today():
        return datetime.now()
class FlyingCar(car):
    def__init__(self, brand, year, origin, speed, number_of_wings):
        super().__init__(brand, year, origin)
        # self.brand = brand
        # self.year = year
        # self.origin =origin
        self.speed =speed
        self.wings =number_of_wings


car_3 = car.alternative_init("BMW-2000-Japan")
print(car_3.__dict__)

print(car_3.today())

# car_1 = car("BMW", 2000)
# car_2 = car("Audi", 2007, "Germany")
# car_1.setting(6)
# print(car_1.number_of_wheels)
# print(car_2.__dict__)
# print(car.__dict__)
