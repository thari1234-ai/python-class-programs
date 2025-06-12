text="seetha"
print("upper=",text.upper())# print upper
text="SEETHA"
print("lower=",text.lower())# print lower
txt = "565543"
x = txt.isnumeric()# check if its all no
print(x)
txt = "Hello"
x = txt.isprintable()# check if its printable
print(x)
txt = "    "
x = txt.isspace()# check spaces 
print(x)
txt = "Hello All!"
x = txt.istitle()#check whether the first character is upper
print(x)
txt = ("Ant", "Bat", "Iron")
x= "Man"
print(x.join(txt))#join both 
txt="HiHello"
print(txt.ljust(10,'+'))#print untill 10 if spaces print+
txt= "        Hello India     "
print(txt.lstrip())#remove spaces in front
txt="rockstar"
mytrans= str.maketrans("r", "R")#which replace strings and characters
print(txt.translate(mytrans))
txt="I could drive all day"
x=txt.partition("drive")#which splits the string
print(x)
txt="I could drive all day"
x=txt.replace("drive","drink")# replace strings
print(x)
txt="i could drive all day"
changed=txt.rfind("drive") #find the index
print(changed)
txt = "Wait for me girls."
x = txt.rindex("girls")#print the index
print(x)
txt="SEETHA"
print(text.rjust(10, '*'))#print * left before gving10 space
txt="I could drive all day"
x=txt.rpartition("drive")#splits into 3 elements
print(x)
txt = "welcome to the sebs"
x = txt.split()#splits into each elements like list
print(x)
txt = "Thank you for the listening\nWelcome to the sebs"
x = txt.splitlines()#to split into each line where we use \n to split 
print(x)
text="seetha"
print(text.startswith("s"))# to check if the character starts with that one
text="tAMiLnAdU"
print(text.swapcase())#to change the upper to lower  and lower to upper vice versa
txt = "Hello"
x = str.maketrans("H", "B")# replace the char
print(txt.translate(x))
x="14"
print(x.zfill(5))# add 0 s at the begining untill it reaches the specified index

