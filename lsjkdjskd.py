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
