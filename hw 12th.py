#1
n = int(input())
if (n % 2) == 0:
    print("Even")
else:
   print("Odd")
#2
n = int(input( ))
if n > 0:
   print("Positive number")
elif n== 0:
   print("Zero")
else:
   print("Negative number")
#3
maths=int(input())
physics=int(input())
chemistry=int(input())
total_marks=maths+physics+chemistry
p=(total_marks)/300
print(total_marks)
print(f"{p}")
if p>90/100:
    print("Eligible")
else:
    print("Not Eligible")
#4
str = str(input())
if str in str.upper():
    print("Upper case")
elif str in str.lower():
    print("Lower case")
else:
    print("Combination of both")

