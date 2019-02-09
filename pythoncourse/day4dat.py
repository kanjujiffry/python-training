#class
# instance/object
# instantiate (called object)
# class PythonProgrammer():
#     beard ="not so much"
#     pass
#
# dev1 = PythonProgrammer()
# dev2 = PythonProgrammer()
# dev1.name ="Daniel"
# dev1.age=25
# dev2.name ="kim"
# dev2.age=23
# print(dev1.name)
# print(dev2.age)
# daniel.beard ="alot"
# print(kim.beard)
# print(daniel.beard)

# class PythonProgrammer():
#     course = "python 0 to 1"
#     def__init__(self, beautiful_name, nice_age,last_name):
#         self.name = beautiful_name
#         self.age = nice_age
#         self.email = f"{beautiful_name}.{nice_age}@gmail.com"
#         self.lastname =last_name
#
# dev1 = PythonProgrammer("daniel",25"sexton")
# dev2 = PythonProgrammer("kim",23"deua")
# dev1.course ="Python 0 to 2"
# print(dev1.course)
# print(dev1.__dict__)
# print(dev2.course)
# print(dev2.__dict__)
# print(PythonProgrammer.course)
# print(PythonProgrammer.__dict__)



class Car:
    def__init__(self,brandname,year,origin="America"):
            self.brand =brandname
            self.year=year
            self.orgin =origin
        #regular method
    def  starts (self):
            print("this is {},it is made in {} ".format(self.brand,self.origin,self.year ))
    def just_for_fun(self):
                self.forFun= self.brand+"is stupid!"
                return self.forFun


my_car =Car("BMW",2000)
print(my_car__dict__)
my_friends_car = Car("audi",2007,"Germany")
help(my_car)
