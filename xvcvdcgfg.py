import re

def password(p):
    i=r'^(?=.+[a-zA-Z]).{8,}.*[1]$'
    if re.match(i,p):
        print("strong")
    else:
        print("not")
password('THARSKDJSDajshakldnskdJLS1')