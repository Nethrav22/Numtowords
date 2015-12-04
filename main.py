#!/usr/bin/python3

#Nethra and Zach Schlotman Colab
def sing( n ):
	if n == 1:
		return "one"
	elif n == 2:
		return "two"
	elif n == 3:
		return "three"
	elif n == 4:
		return "four"
	elif n == 5:
		return "five"
	elif n == 6:
		return "six"
	elif n == 7:
		return "seven"
	elif n == 8:
		return "eight"
	elif n == 9:
		return "nine"
	elif n == 0:
		return " "
	else:
		return "error"
def conv(n):
	if n < 100:
		if n//10 == 1:
			return "ten-"
		elif n//10 == 2:
			return "twenty-"
		elif n//10 == 3:
			return "thirty-"
		elif n//10 == 4:
			return "fourty-"
		elif n//10 == 5:
			return "fifty-"
		elif n//10 == 6:
			return "sixty-"
		elif n//10 == 7:
			return "seventy-"
		elif n//10 == 8:
			return "eighty-"
		elif n//10 == 9:
			return "ninty-"
		else:
			return " "
	#elif n == 100:
	#	return "onehundred"
	elif n < 1000:
		return sing(n//100) + "-hundred-"
	#elif n == 1000:
	#	return "thousand"
	elif n < 10000:
		return sing(n//1000) + "-thousand-"
	elif n == 10000:
		return "ten-thousand"
	else:
		#i = n;
		#j = 1
		#while(i > 0):
		#	j*=10
		#	i//=10
		#sing(n // j) + "-thousand"
		return " "
def teen(n):
	if(n == 11):
		return "eleven"
	elif(n == 12):
		return "twelve"
	elif(n == 13):
		return "thirteen"
	elif(n == 14):
		return "fourteen"
	elif(n == 15):
		return "fifteen"
	elif(n == 16):
		return "sixteen"
	elif(n == 17):
		return "seventeen"
	elif(n == 18):
		return "eighteen"
	elif (n == 19):
		return "nineteen"
	else:
		return "null"
def main(n):
	if n < 10:
		return sing(n)
	elif n < 20:
		return teen(n)
	elif n < 100:
		return conv(n)
	elif n < 1000:
		return conv(n) + conv(n%100) + sing(n%10)
	elif n < 10000:
		return conv(n) + conv(n%1000) + conv(n%100) + sing(n%10)
while(1 == 1):
	n = input("Enter String of integers:")
	print(main(int(n)))
