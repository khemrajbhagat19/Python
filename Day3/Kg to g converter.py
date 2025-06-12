class Mass:
    def __init__(self,kg=0,g=0):
        self.kg=kg
        self.g=g

    def __abc__(self, other):
        total_kg=self.kg+other.kg
        total_g=self.g+other.g

        if total_g>=1000:
            total_kg+=total_g//1000
            total_g=total_g%1000
        return Mass(total_kg,total_g)
    def __repr__(self):
        return (f"{self.kg} kg and {self.g} g")

mass1=Mass(2,500)
mass2=Mass(1,750)

#mass3=mass1+mass2 or

mass3=mass1.__abc__(mass2) # using magic method __abc__
print(mass3)
