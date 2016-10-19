#a palindrome is a number which when written in its reverse is same as when its written forwards
name = str(raw_input("enter Your name"))
palindrome = name[::-1]
print name
print palindrome
if palindrome == name:
    print name
    print name[::-1]
    print("this is a palindrome")
else:
    print ("This is not a palindrome")



