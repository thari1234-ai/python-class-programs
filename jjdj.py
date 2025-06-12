#2
print("THAR HOTEL WELCOMES YOU")
option = input("Enter your choice (1/2/3/4): ")
 
match option:
    case '1':
        print("\n tiffin Menu:")
        print("1. idly----------$90")
        print("2. dosa---------$1000")
        print("3. poori-----------$80")
 
    case '2':
        print("\n rice:")
        print("1. lemon rice---------$45")
        print("2. tomato rice--------$25")
        print("3. fried Rice---------$30")
 
    case '3':
        print("\n dessert Menu:")
        print("1. tiramisu---------$10")
        print("2. choco lava cake--------$25")
        print("3. icecreamuh----------$30")
 
    case '4':
              quit()
 
    case _:
              print("sorry,we dont have that food")
