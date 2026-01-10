def checkPalindrome(str):
    #Cleaning the string
    clean_str = (str.replace(" ", "")).lower()

    #Reversing the string
    reverse_str = clean_str[::-1]
    return clean_str == reverse_str

str = input("Enter a string: ")

if checkPalindrome(str):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

'''Output:
Enter a string: ABBA
It is a palindrome.
'''