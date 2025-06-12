#1
cosmetics_dict ={
 "lakme": ["foundation", "matte finish lipstick", "eyeliner", "face wash"],
 "maybelline": ["pot kajal", "liner", "lipliner"],
 "fair&lovely": ["face cream", "face wash", "powder"],
 "himalaya": ["face cream", "face wash", "kaajal", "moisturizing cream"],
 "dazzler": ["foundation", "primer", "lipstick", "lip balm", "compact powder"]
}
brand= input("Enter a cosmetic brand: ")
if brand in cosmetics_dict:
    product=(cosmetics_dict[brand])
    print("list of cosmetic products of",brand,"is",product)
else:
    print("Not available")
#2
a = int(input())
b = int(input())
print("1) Add 2) Subtract 3) Multiply 4) Divide 5) Exponent")
option = input("Enter your choice (1/2/3/4/5): ")
match option:
    case "1":
        print("Add")
        sum = a + b
        print(f"{a} + {b} = {sum}")
    case "2":
        print("Subtract")
        dif = a - b
        print(f"{a} - {b} = {dif}")
    case "3":
        print("Multiply")
        pro = a * b
        print(f"{a} * {b} = {pro}")
    case "4":
        print("Divide")
        if b != 0:
            c = a // b
            print(f"{a} // {b} = {c}")
        else:
            print("Error: Division by zero is not allowed.")
    case "5":
        print("Exponent")
        pow = a ** b
        print(f"{a} ** {b} = {pow}")
    case _:
        print("invalid")
