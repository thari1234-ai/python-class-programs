def ecommerce(base,discount,tax):
    if base<0 or discount<0 or tax<0:
        return "error"
    else:
        discount_amount = (discount / 100) * base
        discounted_price = base - discount
        tax_amount = (tax/ 100) * discounted_price
        final_price = discounted_price + tax_amount
        return round(final_price, 2)
try:
    base=float(input())
    discount=float(input())
    tax=float(input())
    e=ecommerce(base,discount,tax)
    print(e)
except ValueError:
    print("ERROR")

               