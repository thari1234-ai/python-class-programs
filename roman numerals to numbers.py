def roman_to_int(roman):#roman=xxxiv 
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]
    result = 0
    n = len(roman)#5
    for i in range(n):
        current_index = roman_numerals.index(roman[i])#X=10
        if i < n - 1 and roman_values[current_index] < roman_values[roman_numerals.index(roman[i + 1])]:
            #SINCE OME IS COMBINED LIKE THIS 1V SO i<V which less then so 30-1=29
            #AFTER 29 IT WILL ITERATTE THE LAST V 29+5=34 cuz last p
            result -= roman_values[current_index]
        else: 
            result += roman_values[current_index] #29+5=4

    return result#34
print(roman_to_int("XXXIV")) 
