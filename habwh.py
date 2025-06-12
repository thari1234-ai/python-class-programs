#1
n=int(input())#18
last=n%10#18%10=8
first=n//10#8#18//10=1
x=first+last#1+8=9
str1=str(x)#"9"
for i in str1:
    if x%9==0:#9%9==0
        print(f"{x} is a Harshad Number")
    else:
         print(f"{x} is not Harshad number")
#2
n = int(input("Enter the number of students: "))# no of students #3
total_books = 0#initial 0 sum |1|3|6
books_read = input()# 1,2,3
books_list = [int(x) for x in books_read.split(",")]# to convert into list integers seperated by commas
#["1","2","3","4]"
for i in books_list:
    total_books += i#0+1=1|2+1=3|3+3=6|4+6=10
print(f"{total_books}")#10
#3
n=int(input())#3
for i in range(1,n+1,1):#1,4,1
    for j in range (i):#column
        print("*",end ="")# * print
    print()

