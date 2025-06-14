class Father:
    money=1000
    def show(self):
        print("Parent class instance method")
    @classmethod
    def moneyshow(cls):
        print("Parent Class Class Method: Total money = ",cls.money)
    @staticmethod
    def stat_method():
        a=5
        print("Parent Class Static Method: the value of a is ",)