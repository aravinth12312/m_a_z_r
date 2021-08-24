def traingle(data,n):
	#hi
	k = 2*n - 2
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 2
		for j in range(0, i+1):
				print("%s "%(data[j]), end="")
		print("\r")

def manipulate(data):
	temp=[]
	if len(data)%2==1:
		temp.append(data[len(data)//2:])
		temp.append(data[:len(data)//2])
		res="".join(temp)
	else:
		res=data
	return res

data=input()
n=len(data)
traingle(manipulate(data),n)
#
#
#
#
#
#
