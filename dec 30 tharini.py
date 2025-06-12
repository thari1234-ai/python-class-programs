class alphanumsppl:
    def __init__(self, input_string):
        self.input_string = input_string
        self.spl = "!@#$%^&*"  
        self.count_alpha = 0
        self.count_num = 0
        self.count_spl = 0

    def alphabets(self):
        for i in self.input_string:
            if i.isalpha():
                self.count_alpha += 1

    def numbers(self):
        for i in self.input_string:
            if i.isdigit():
                self.count_num += 1

    def special_characters(self):
        for i in self.input_string:
            if i in self.spl:
                self.count_spl += 1

    def display_results(self):
        # Print the results
        print(self.count_alpha) 
        print(self.count_num)  
        print(self.count_spl) 
n = input("Enter a string: ")


s= alphanumsppl(n)

s.alphabets()
s.numbers()
s.special_characters()
s.display_results()
class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string
        self.spl = "@#$%^&*!"  
        self.count_alphaa = 0
        self.count_spla = 0

    def count_characters(self):
        for i in self.input_string:
            if i in self.spl:
                self.count_spla += 1
            elif i.isalpha():
                self.count_alphaa += 1

    def check_characters(self):
        if self.count_spla > 0 and self.count_alphaa > 0:
            print("The string contains both alphabets and special characters")

    def display_results(self):
        print("Number of alphabets:", self.count_alphaa)
        print("Number of special characters:", self.count_spla)

n = input("Enter a string: ")
a = StringAnalyzer(n)
a.count_characters()
a.check_characters()
a.display_results()
