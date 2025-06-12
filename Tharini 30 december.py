n=input()
count_alpha=0
count_num=0
count_spl=0
spl="!@#$%^&*"
for i in n:
    if i.isalpha():
        count_alpha+=1
    elif i.isalnum():
        count_num+=1
    elif i in spl:
        count_spl+=1
print(count_alpha)
print(count_num)
print(count_spl)

n = input()  
spl = "@#$%^&*!"  
count_alphaa = 0
count_spla = 0
for i in n:
    if i in spl:  
        count_spla += 1
    elif i.isalpha():  
        count_alphaa += 1
    if count_spl > 0 and count_alpha > 0:
        print("The string contains both alphabets and special characters")
        break 