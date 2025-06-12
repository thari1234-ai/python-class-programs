n = int(input("Enter the number of students: "))
total_books = 0
books_read = input()
books_list = [int(x) for x in books_read.split(",")]
for i in books_list:
    total_books += i
print(f" {total_books}")
