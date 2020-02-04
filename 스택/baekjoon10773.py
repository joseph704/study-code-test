case_num = int(input())
list = list()
for i in range(case_num):
	a = int(input())
	if a!=0:
		list.append(a)
	else:
		try:
			list.pop()
		except:
			pass
print(sum(list))