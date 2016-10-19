#practise2:
#asks user to enter 2 numbers check if numder is even or odd
#also check if number is a divisible by 4
num1 = input("Enter your first number")
check = input("Enter your second number")
if int(num1%2 == 0): 
	print (num1,"hello pretty one, your number is Even")
elif num1%2 != 0:
	print("Get over it, Your Number is odd")
if check%4 == 0:
	print("Divisible by 4")
else:
		print("Lets wrap things up!!!!!!!!!!!!!!!go Home")