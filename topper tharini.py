class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def avg_marks(self):
        return sum(self.marks.values())/len(self.marks)
s=[
    Student(input(),int(input()),{input():int(input()),"ai":100}),
    Student("Asiya",2,{"maths":10,"ai":20})
    ]
topper=max(s,key=lambda s:s.avg_marks())
print(topper.name)
print(topper.roll)
print(topper.marks)