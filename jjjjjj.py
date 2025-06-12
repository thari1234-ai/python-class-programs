import math
bill1=int(input())
bill2=int(input())
bill3=int(input())
print("The bill cost",bill1+bill2+bill3)
total_bill=bill1+bill2+bill3
tax_amount=total_bill*0.0675
total_tax=total_bill+tax_amount
tip=int(tax_amount*0.1)
if(bill1+bill2+bill3>400):
    print("The tax amount:",math.floor((total_bill*0.0675)))
    print("tip",int((tax_amount*0.1)))
    print("The total amount:",int(total_bill+tax_amount+tip))
