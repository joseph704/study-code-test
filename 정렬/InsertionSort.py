def InsertionSort(list,n):
	for i in range(1,n):
		key = list[i]
		j=i-1
		while j>=0 and list[j]>key:
			list[j+1] = list[j]
			j=j-1
		list[j+1] = key

list = [2,3,6,3,1,2,67]
InsertionSort(list,len(list))
print(list)