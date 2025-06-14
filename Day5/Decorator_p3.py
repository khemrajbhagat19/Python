def abc(func): # decor function
    def inner():
        print("-------------")
        func()
        print("-------------")
    return inner
@abc # here abc is decor function
def msg():
    print("Python Programming")

msg()