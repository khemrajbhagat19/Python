def decor(func):
    def inner():
        print("-------------")
        func()
        print("-------------")
    return inner
@decor
def msg():
    print("Python Programming")

msg()