s=input()
vowel=0
m=set("aeiouAEIOU")
for i in s:
    if i in m:
        vowel+=1
print(vowel)
