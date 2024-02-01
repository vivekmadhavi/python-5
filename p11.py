#sp -> DIY

n= int(input("enter the first value"))
r= int(input("enter the second value"))


r1=1
for i in range(1,n+1):
	r1=r1+i	
r2=1
for i in range(1,n+1):
	r2=r2+i	

r3=1
for i in range(1,n+1):
	r3=r3+i		
		
res= r1/(r2*r3)
print(res)


