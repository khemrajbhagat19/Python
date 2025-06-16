from time import sleep
students=["Atul","Naveen","Rakhi","Anmol","Neha","Ayush"]
def read():
    sleep(3)
    print("Reading done....")
    data=students
    while True:
        name=(yield ) # execution suspend
        if name in data:
            print("Found")
        else:
            print("Not Found")

search=read()
print("Reading all data....")
next(search)
next(search)
search.send("Arvind")
search.send("Rakhi")
