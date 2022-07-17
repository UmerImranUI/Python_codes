def fib(n):
	first=0
	second=1
	next=0
	for i in range (1,n+1):
		if (n<=1):
			next=i
			break
		else:
			next=first+second
			first=second
			second=next
	return next
n=int(input("enter the number you want: "))
a=fib(n)
print(a)
