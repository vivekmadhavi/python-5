#wapp to square the given number



def comput(n1,n2,n3):
	sum = n1+n2+n3
	avg=(sum)/3
	return sum,avg
	

n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the  third number"))
sum,avg=comput(n1,n2,n3)
print("sum =",sum)
print("avg =",avg)