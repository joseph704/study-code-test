case_num = int(input())
grpcount = []
for i in range(case_num):
	word = list(map(str,input()))

	for j in range(len(word)):
		if j != len(word)-1 and word[j] == word[j+1]:
			pass
		elif word[j+1:].count(word[j])!=0:
			break
		elif j==len(word)-1:
			grpcount.append(i)

print(len(grpcount))