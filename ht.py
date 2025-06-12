#1
number=int(input())
if((number % 3 == 0) and (number % 5 == 0)):
    print("combination of both")
elif number%3==0:
    print("divisible by 3")
elif number%5==0:
    print("divisible by 5")
else:
    print("not divisible")
#2
import math
bill1=int(input())
bill2=int(input())
bill3=int(input())
print("The bill cost",bill1+bill2+bill3)
total_bill=bill1+bill2+bill3
tax_amount=total_bill*0.0675
total_tax=total_bill+tax_amount
tip=int(total_tax*0.1)
if(bill1+bill2+bill3>400):
    print("The tax amount:",math.floor((total_bill*0.0675)))
    print("tip",int((total_tax*0.1)))
    print("The total amount:",int(total_bill+tax_amount+tip))
else:
    print(total)
#3
weight=float(input())
height=float(input())
bmi=weight/height**2
print(int(bmi))
if bmi<16:
    print("severe thinness")
elif 16<bmi<17:
    print("moderate thinness")
elif 17<bmi<18.5:
    print("mild thinness")
elif 18.5<bmi<25:
    print("normal")
elif 25<bmi<30:
    print("over weight")
elif 30<bmi<35:
    print("obese class I")
elif 35<bmi<40:
    print("obese class II")
elif bmi>40:
    print("obese classIII")
else:
    print("check your height and weight")
