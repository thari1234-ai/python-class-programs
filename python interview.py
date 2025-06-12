s=input()
spl_char=set("@#$!%^&*")
se=""
spl=""
for i in s:
    if i in spl_char:
        spl+=i
    elif i not in spl_char:
        se+=i
reverse=se[::-1]       
z=reverse+spl
print(z)