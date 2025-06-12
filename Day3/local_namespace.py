class XYZ:
    def my_func():
        a=5
        b=15
        c=20
        print("In Local")
        print(dir())
        def inner():
            a=5
            print("In Inner")
        inner()
        print(dir())
    my_func()

print(dir(XYZ))

