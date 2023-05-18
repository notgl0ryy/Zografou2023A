string=input("enter a string:")
i=int
for i in string:
    reversed=reversed+i
    if string==reversed:
        print("the string is a palindrome.")
    else:
        print("the string is not a palindrome.")