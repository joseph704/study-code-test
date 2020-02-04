N = int(input())

for i in range(1,N+1):
	sum = i
	ii = str(i)
	for j in range(len(ii)):
		sum += int(ii[j])
	if sum==N:
		print(i)
		break
	else:
		pass
if sum!=N:
	print(0)