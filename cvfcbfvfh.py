def roman_to_int(roman):#roman=xxxiv 
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    result = 0
    n = len(roman)#5
    for i in range(n):#5
        current_index = roman_numerals.index(roman[i])
print(current_index)
roman_to_int('XXXIV')        