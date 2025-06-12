def roman(n):
    roman_numerals = {
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    }
    result=0
    i=0
    while i<len(n):
        if i + 1 < len(n) and n[i:i+2] in roman_numerals:
            result += roman_numerals[n[i:i+2]]
            i += 2
        else:
            result += roman_numerals[n[i]]
            i += 1
    return result
print(roman("XXXIV"))  # Output: 34




            
