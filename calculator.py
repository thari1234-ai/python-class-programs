class Calc:
    def __init__(self, a, b): 
        if b == 0:
            raise ZeroDivisionError("Number cannot be divisible by 0")
        
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Non-numeric is not cool dude use num ")
        
        special_chars = "@#$%^&*"
        for char in str(a) + str(b):
            if char in special_chars:
                raise ValueError("no! special symbols @#$%^&*")
            break 
        self.a = a  
        self.b = b  
        self.operations = {"add": self.addition, "sub": self.subtraction}  

    def calculate(self, op):# for key error for sub and add
        if op not in self.operations:#if it is not sub or add it will give key error cuz it doesnt matches 
            raise KeyError(f"Invalid operation: {op}")
        return self.operations[op]() #return the value

    def addition(self):
        add = self.a + self.b
        return add 

    def subtraction(self):
        sub = self.a - self.b
        return sub 

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter the operation (add/sub): ")#options are add and sub
    c = Calc(a, b)  
    result = c.calculate(op) 
    print(result)

except ZeroDivisionError:
    print("Number cannot be divisible by 0")
except TypeError:
    print("Non-numeric is not cool dude use num ")
except ValueError:
    print("no! special symbols @#$%^&*")
except KeyError:
    print("invalid operation")
except Exception as e:
    print("An unexpected error occurred:", e)