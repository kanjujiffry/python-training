# class method
@classmethod
def setting(cls,number):
    cls.number_of_wheels = number
@classmethod
def alternative_init(cls,string)
# string ="bmw-2000-Japan"
brand,year,origin= string.split("-")
retun cls(brand,year,origin)
@staticmethod
def today():
    retun datetime.now
# car _1 =Car ("BMW",2000)

car_2 =Car ("Audi",2005,"Germany")
# print(car_1.number_of_wheels)
# print(car_2.number_of_wheels)
# print(car.number_of_wheels)
#
car_1.setting(6)

print(car_1.number_of_wheels)
print(car_2.__dict__)
print (Car.__dict__)
