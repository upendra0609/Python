def add(a, b):
    print(a + b)


add(5, 8)


# key parameter
def greet(name, dept):
    print(f"hi {name}")
    print(f"are you from {dept} department?")


greet("A", dept="CS")


# var args parameter
def sum_num(*numbers):
    s = 0;
    for i in numbers:
        s += i
    print(s)


sum_num(1, 2, 3, 4)
sum_num(6, 4, 3, 2, 5, 7)


# *kwargs
def info(**emp):
    for key, value in emp.items():
        print(key, value)


info(name="AA", age=12, eid="123")
info(name="BB", eid="123")
info(name="AA", age=12, eid="123", mobile="1234567890")

# (*args, **kwargs)   valid
# (**kwargs,*args)   invalid
