
#1
a = 4
b = 5
min_value = a if a < b else b # Ternary operator to find the minimum
print(f"{min_value}")
#2
import math
principle= float(input('Enter amount: '))
time= float(input('Enter time: '))
rate = float(input('Enter rate: '))
amount = principle* (1 + (rate / 100)) ** time
ci = amount - principle
ci=ci//100 #3 digit 
print(int(ci))
#3
x = int(input())
y = int(input())
x, y = y, x
print(f"{x} {y}")
#4
list = [1, 6, 3, 5, 3, 4]
print("present?",6 in list)
#5
str=("mia","pia","cia")
print("mia" in str)
