''' Accept char from the user findout given character is vowel or not'''

ch=input("Enter any char: ")
lst=['a','e','i','o','u','A','E','I','O','U']
#Conditional Statement
if ch in lst:
    print("Vowel")
else:
    print("Not a Vowel")

#Conditional Operator
print("Vowel") if ch in lst else print("Not a vowel")
