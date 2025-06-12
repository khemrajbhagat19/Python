class Time:
    def __init__(self,year=0,month=0):
        self.year=year
        self.month=month

    def __abe__(self, other):
        total_year=self.year+other.year
        total_month=self.month+other.month

        if total_month>=12:
            total_year+=total_month//12
            total_month=total_month%12
        return Time(total_year,total_month)
    def __repr__(self):
        return (f"{self.year} year and {self.month} month")

Time1=Time(2,12)
Time2=Time(1,6)

#mass3=mass1+mass2 or

Time3=Time1.__abe__(Time2) # using magic method __abc__
print(Time3)
