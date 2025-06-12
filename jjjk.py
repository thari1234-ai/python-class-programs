import math
item1=int(input())
item2=int(input())
item3=int(input())
bill_cost = item1 + item2 + item3
if bill_cost > 400:
    tax_rate = 0.0675
else:
    tax_rate = 0 
    tax_amount = bill_cost * tax_rate
    total_with_tax = bill_cost + tax_amount
    tip_amount = total_with_tax * 0.10
    final_total = total_with_tax + tip_amount
    print(tax_amount)
    print(total_with_tax)
    print(tip_amount)
    print(final_amount)
