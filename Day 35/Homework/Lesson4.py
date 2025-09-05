def palindrome(s):
    s = s.lower()
    return s == s[::-1]  

print(palindrome("wow"))  
print(palindrome("hello"))  
print(palindrome("A man a plan a canal Panama"))  
