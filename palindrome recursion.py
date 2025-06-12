def palindrome(s):
    if len(s)<=1:
        return "palindrome"
    elif s[0]!=s[-1]:
        return "False"
    return palindrome(s[1:-1])
result=palindrome("madam")
print(result)