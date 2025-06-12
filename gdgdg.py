import re

def password(p):
    
    i=r'(?=.+*[a-z].{12}+.*[A-Z]{3}![!@#$%^&*]!/d)$'
    if re.match(i,p):
        print("strong")
    else:
        print("not")
p=input()
password(p)