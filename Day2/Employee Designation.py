class Employee:
    office_name="NIET"
    def __init__(k,name,designation): # k is constructor
        k.name=name
        k.designation=designation

    def show_detail(k):
        print(k.name, k.designation)

m1=Employee("RAJ","Manager") # m1,m2 are objects/instances
m2=Employee("Manish","HR")
m1.show_detail()
m2.show_detail()