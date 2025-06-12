class Distance:
    def __init__(self,km=0,m=0):
        self.km=km
        self.m=m

    def __adc__(self, other):
        total_km=self.km+other.km
        total_m=self.m+other.m

        if total_m>=1000:
            total_km+=total_m//1000
            total_m=total_m%1000
        return Distance(total_km,total_m)
    def __repr__(self):
        return (f"{self.km} km and {self.m} m")

Distance1=Distance(2,500)
Distance2=Distance(1,750)

Distance3=Distance1.__adc__(Distance2)
print(Distance3)
