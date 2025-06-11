class MathOperations:
    @staticmethod
    def add_numbers(a,b):
        return a+b
    @staticmethod
    def subtract_numbers(a,b):
        return a-b
obj=MathOperations()
result_add=MathOperations.add_numbers(10,5)
result_subtract=MathOperations.subtract_numbers(10,5)

print(f"Addition : {result_add}")
print(f"Subtraction : {result_subtract}")