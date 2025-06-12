item1 = float(input("Enter cost of item 1: "))
item2 = float(input("Enter cost of item 2: "))
item3 = float(input("Enter cost of item 3: "))
bill_cost = item1 + item2 + item3
if bill_cost > 400:
    tax = bill_cost * 0.0675
    tip = (bill_cost + tax) * 0.1
    total = bill_cost + tax + tip
print("Bill Cost: Rs.", bill_cost)
print("Tax Amount: Rs.", tax)
print("Tip Amount: Rs.", tip)
print("Total Amount: Rs.", total)


