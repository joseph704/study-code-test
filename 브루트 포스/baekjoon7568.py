case_num = int(input())
list = []
for i in range(case_num):
	list.append(tuple(input().split()))

for j in range(case_num):
	rank = 1
	for k in range(case_num):
		if list[j][0]<list[k][0] and list[j][1]<list[k][1]:
			rank += 1
	print(rank,end=' ')