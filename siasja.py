#1
t = input("Enter transaction id: ")  # 456
reversed_int = ""  # stores as empty string 
for i in range(len(t) - 1, -1, -1):# len(t)-1= last index,-1=stop.-1=step
    reversed_int += t[i]# t[0]=4,t[1]=5,t[2]=6  from reverse it will print

print("Reversed id:", reversed_int)#reversed id is printed 
#2
while True:# to repeat from 1st after 4digit
    t = input("Enter a 3-digit number: ")
    
    if len(t) != 3:
        print("3digit only")
        continue  # Restart the loop 
    
    first = int(t[0])
    second = int(t[1])
    third = int(t[2])
    powers = len(t)
    
    sum_of_cubes = first**powers + second**powers + third**powers
    g= int(t)
    
    if sum_of_cubes == g:
        print(f"{g} is  Armstrong number.")
    else:
        print(f"{g} is not  Armstrong number.")
    
    break  # Exit the loop 


