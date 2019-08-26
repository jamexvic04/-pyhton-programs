def ispalindrome():
    a_str = str(input("enter any word: "))
    a_str = a_str.casefold()
    rev_str = reversed(a_str)
    if list(a_str) == list(rev_str):  
        print("it is a palindrome")  
    else:  
        print("it is not a palindrome")
ispalindrome()