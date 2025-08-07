""" 
Note: 
In LeetCode, there is a requirement of removing special characters before checking.
Normally, if we only check for a pharse, we can just compare with reversed slicing.

TL;DR: 
isPalindrome() is for LeetCode test.
simple_check_palindrome() is written by my reflex.
"""

def isPalindrome(s: str) -> bool:
    s = s.lower()
    s_cleaned = ''.join([(char if char.isalpha() else '') for char in s])
    s_reverse = ''.join(s_cleaned[::-1])
    return s_cleaned == s_reverse

def simple_check_palindrome(s: str) -> bool:
    s = s.lower()
    return s[::] == s[::-1]
    #return s == ''.join(reversed(s))

test_cases = ["A man, a plan, a canal: Panama","race a car", " "]
for test_case in test_cases:
    print (f"{simple_check_palindrome(test_case)}\t: \"{test_case}\"")