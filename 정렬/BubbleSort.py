def BubbleSort(list,n):
	for j in range(n):
		for i in range(0,n-1):
			if list[i]>list[i+1]:
				list[i],list[i+1]=list[i+1],list[i]
	n=n-1

list = [5,6,77,3,5,3,6,2,1]
BubbleSort(list,len(list))
print(list)