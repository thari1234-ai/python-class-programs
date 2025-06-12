#basic class programs
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print( f"Hello, my name is {self.name} and I am {self.age} years old.")
p=Person("Tharini",18)
p.display()
#area and peri of rect
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        w=self.length*self.breadth
        print(w)
    def perimeter(self):
        s=2*(self.length+self.breadth)
        print(s)
c=Rectangle(2,4)
c.area()
c.perimeter()

#
#bank account
class Bank:
    def __init__(self,account_no,balance):
        if balance<0:
            return "error"
        self.account_no=account_no
        self.balance=balance

        
    def deposit_d(self):
        deposit=int(input("deposit ammount"))
        self.balance+=deposit
        print("deposit",self.balance)
    def withdraw_w(self):
        withdraw=int(input("withdraw amount"))
        self.balance-=withdraw
        print("withdrawed",self.balance)
    def show_balance(self):
        print("balance",self.balance)
try:
    account_no=int(input("account no"))
    balance=int(input("balance"))
    b=Bank(account_no,balance)
    b.deposit_d()
    b.withdraw_w()
    b.show_balance()
except:
    print("error")
    
#book
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def Book_details(self):
        print(self.title)
        print(self.author)
        print(self.price)
    def discount(self):
        discount_d=int(input())
        discounted_price=self.price-(self.price*discount_d/100)
        print(discounted_price)
b=Book("BOOK","AUTHOR",500)
b.Book_details()
b.discount()
  #is_pass to check if a student is pass or fail
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def is_pass(self):
        if self.marks>=40:
            return "PASS"
        else:
            return "FAIL"
    def display(self):
        print(self.name)
        print(self.roll_no)
        print(self.marks)
        print(self.is_pass())
s=Student("name",100,100)
s.display()
