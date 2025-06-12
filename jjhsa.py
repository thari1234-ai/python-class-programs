n = int(input("Enter the number of students: "))# no of students #
total_books = 0#initial 0 sum |1|3|6
books_read = input()# 1,2,3
books_list = [int(x) for x in books_read.split(",")]# to convert into list integers seperated by commas
if n<3:
    print("only 3 no s")
for i in books_list:
 total_books += i#0+1=1|2+1=3|3+3=6|4+6=10
print(f"{total_books}")#10
