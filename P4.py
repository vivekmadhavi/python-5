#wapp to read astring and check
#it its a palindrome
#string read same from L to R and R to L
#eg : racecar, wow, lol , mom , pop , malay


str=input("enter the palindrom")

r1= str[::-1]
r2= str[:]

if r1==r2 :
	print(" it is palindrome")
else:
	print("it is not palindrom")


# logic 2

str = input("enter a string")
print("yes" if str == str[::-1] else "no")
