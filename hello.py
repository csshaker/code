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
			
def isEven(number):
	if number % 2 == 0:
		return True
	else:
		return false

def arraySum(li):
	summation = 0

	for i in range(li):
		summation += i

	return summation

def isPrime(number):
	i = 2

	while i <= number / 2:
		if number % i == 0:
			return False
	
	return True

def primeGenerator(n):
	prime = []
	i = 2

	while i <= n:
		if isPrime(i):
			prime.append(i)

	return prime

def evenGenerator(n):
	even = []
	i = 1

	while i <= n:
		if isEven(i)
			even.append(i)

def hello():
	print("hello")
	return even

def logout():
	print('log out')