def is_palindrome(str):
    reverse_str = ''.join(reversed(str))
    if str == reverse_str :    
        print("It is palindrome")
    else:
        print("It is not polindrome")

str = str(input())

is_palindrome(str)
