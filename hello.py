def func_signup():
	print("sign up")
	
def subtraction(a, b):
	return a - b
	
def addition(a, b):
	return a + b
	
def multiplication(a, b):
	return a * b

def printSomething(something):
	print(something)

def division(a, b):
	try:
		return a / b
	except ZeroDivisionError:
		print("cannot divide by zero")

def maxThree(num1, num2, num3):
	if num1 > num2:
		if num1 > num3:
			return num1
		else 
			return num3
	else:
		if num2 > num3
			return num2
		else
			return num3
			
def isEven(number):
	if number % 2 == 0:
		return True
	else:
		return false
