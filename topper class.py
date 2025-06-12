class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def avg_marks(self):
        return sum(self.marks.values())//len(self.marks)
s=[
    Student("alice",101,{"maths":100,"eng":100}),
    Student("madhu",100,{"maths":100,"eng":100})
    ]
topper=max(s,key=lambda s:s.avg_marks())
print(f"Topper: {topper.name} (Roll No: {topper.roll}) with Average Marks: {topper.avg_marks():.2f}")
    