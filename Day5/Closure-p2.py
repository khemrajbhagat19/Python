def outerfunc(x):
    def innerfunc():
        print(x)
    return innerfunc()
myfunc=outerfunc(7)
