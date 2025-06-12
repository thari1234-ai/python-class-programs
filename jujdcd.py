
ftotal = int(input("Enter Flipkart total price: "))
ftax = int(input("Enter Flipkart tax: "))
fshipping = int(input("Enter Flipkart shipping: "))

stotal = int(input("Enter Snapdeal total price: "))
stax = int(input("Enter Snapdeal tax: "))
sshipping = int(input("Enter Snapdeal shipping: "))

atotal = int(input("Enter Amazon total price: "))
atax = int(input("Enter Amazon tax: "))
ashipping = int(input("Enter Amazon shipping: "))

# Calculate the final prices for each platform
flip = (ftotal + ftax + fshipping )// 2
snap =(stotal + stax + sshipping) // 2
amazon =(atotal + atax + ashipping) // 2

# Determine the platform with the lowest price
if ((flip < snap) and (flip < amazon)):
    print(f"In Flipkart: {flip}\nIn Snapdeal: {snap}\nIn Amazon: {amazon}\nChoose Flipkart")
elif ((snap < flip) and (snap < amazon)):
    print(f"In Flipkart: {flip}\nIn Snapdeal: {snap}\nIn Amazon: {amazon}\nChoose Snapdeal")
else:
    print(f"In Flipkart: {flip}\nIn Snapdeal: {snap}\nIn Amazon: {amazon}\nChoose Amazon")
