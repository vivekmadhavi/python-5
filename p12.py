#sp -> DIY

def fact(num):
	f =1
	for i in range(1,num+1):
		f=f*i
	return f	

n= int(input("enter the first value"))
r= int(input("enter the second value"))
			
res= fact(n)/(fact(r)*fact(n-r))
print(res)


