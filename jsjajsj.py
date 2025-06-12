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
bill=int(input())        
tax=int(input())
tips=int(input())
total=bill+tax+tips
if total>400:
    bill=bill*0.0675
    total=total*0.1
    print(total)
    print(bill)
    print(tax)
    print(total)
#3
weight=float(input())
height=float(input())
bmi=weight/height**2
print(bmi)
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
    
             
             

    
