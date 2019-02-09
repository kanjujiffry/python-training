#function
def say_hi(name):
    """
    this functin say to the name
    """
    return "hi,{}".format(name)

print(say_hi.__doc__)

# annotation
def say_hello(name:str)-> str:
    """
    DOCSTRING
    """
    return "Hi"+name

print(say_hello.__doc__)
print(say_hello.__annotations__)
# print()
# print(say)
#with/without return
def add1(*argv):
    sum=0
    for arg in argv:
        sum = sum + arg
    return sum
def add2 (*args):
    sum=0
    for arg in args:
        sum =sum + arg
    print(sum)
def add3(*args):
    sum=0
    for arg in args:
        sum = sum + arg
example1 = add1(1, 2, 3, 4, 5)
print(example1)
add2(1, 2, 3, 4, 5)
