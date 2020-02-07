def selectionSort(list,n):
	for i in range(0,n-1):
		least = i
		for j in range(i+1,n):
			if list[j]<list[least]:
				least = j
			list[i],list[least]=list[least],list[i]

list = [3,5,2,6,8,4,6,1]
selectionSort(list,len(list))
print(list)