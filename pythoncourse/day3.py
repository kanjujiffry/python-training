
# a + b =c
def sum(first,second):
     result = first + second
     return result

r1 = sum(1,2)
r2 = sum (3,5)
r3 = sum (199,456)

print (r1,r2,r3)

def say_hi():
    print("Hello Friend !")
say_hi()

def say_hello(*args):
    for arg in args:
        print(f"Hello,{arg}")

def say_hello(*args ,**kwargs):

    print(args)
    print(kwargs)

say_hello("kim","kanju",age="20",heigh=180)
def say_hello(*args ,**kwargs):
    for arg in args:
    print(args)
    print(kwargs)
for kwarg in kwargs:
    print(kwargs[kwarg])
say_hello({"kim","kanju",age="20",heigh=180)
