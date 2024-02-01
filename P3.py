#wapp to read the name of the user
#and print it in reverse fashion


name=input("enter ur name")

r1 =""
for n in name:
	r1=n+r1

r2 =name[::-1]

print(name)
print(r1)
print(r2)