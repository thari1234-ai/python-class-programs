#1
i = 1
print("Even numbers:")
while i <= 10:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
print()

print("Odd numbers:")
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
print()
#2
x= input("Enter a string: ")
x = x.upper()
reversed_string = ""
for i in range(len(x) - 1, -1, -1):
    reversed_string += x[i]
print("Reversed string:", reversed_string)

x = input("Enter a string: ")
x= x.upper()
reverse = ""
index = len(x) - 1
while index >= 0:
    reverse += x[index]
    index -= 1
print("Reversed string:", reverse)

#3
s = [150, -20, 300, -50, 200, -10, 400, -30]
successful = 0
losses = 0
for n in s:
    if n > 0:
        successful += 1
    elif n < 0:
        losses += 1
print("Number of successful sales:", successful)
print("Number of returns or losses:", losses)
  
    

 
