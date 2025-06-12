N=int(input())
number=[]
for i in range(N):
    num=int(input(f'Enter numbere{i+1}'))
    number.append(num)
even=0
odd=0
for num in number:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)
            