def print_name(prefix):
    print(f"Searching Prefix: {prefix}")
    while True:
        name=(yield) # execution suspended
        if prefix in name:
            print(name)

corou=print_name("Dear")

corou.__next__()

corou.send("Atul")
corou.send("Dear Atul")