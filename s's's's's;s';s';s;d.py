
a = int(input( ))
b = int(input())
print("1) Add 2) Subtract 3) Multiply 4) Divide 5) Exponent")
option = input("Enter your choice (1/2/3/4/5): ")
match option:
 case "1":
     print("Add")
     sum = a + b
     print(f" {a} + {b} = {sum}")
 case "2":
     print("Subtract")
     dif = a - b
     print(f" {a} - {b} = {dif}")
 case "3":
     print("Multiply")
 pro = a * b
 print(f" {a} * {b} = {pro}")
 case "4":
 print("Divide")
 if b != 0:
 c = a // b
 print(f" {a} // {b} = {c}")
 else:
 print("Error: Division by zero is not allowed.")
 case "5":
 print("Exponent")
 pow = a ** b
 print(f" {a} ** {b} = {pow}")
 case _:
 print("You have selected an invalid option.")
