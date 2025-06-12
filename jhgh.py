t = input("Enter a 3-digit number: ")
if len(t) != 3:#if itsnot three digit it will not print 
    print("3 digit only acceptable")
    quit()# to quit because it is not 3 digit 
else:
    first = int(t[0])# 1st index of t
    second = int(t[1])#2nd index
    third = int(t[2])#3rd index
    powers=len(t)#counting the input 
    sum_of_cubes = first**powers + second**powers + third**powers
    g = int(t)#assigning the value as t
    if sum_of_cubes == g:# if user and sum is equal it will print armstrong
        print(f"{g} is armstrong number")
    else:
        print(f"{g} is not armstrong number")
