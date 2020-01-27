num = int(input())
roomlist = []
for i in range(num):
	a,b,c = map(int,input().split())
	if c%a!=0:
		Y = c%a
	else:
		Y = a
	if c%a!=0:
		X = c//a+1
	else:
		X = c//a
	if X<10:
		X="0"+str(X)
	roomlist.append(str(Y)+str(X))

for i in roomlist:
	print(i)
