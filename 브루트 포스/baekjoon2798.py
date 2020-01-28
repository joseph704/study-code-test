Num,Max = map(int,input().split())
list=list(map(int,input().split()))
sumlist=[]
blackjack = []
if len(list)==Num:
	for i in range(len(list)):
		for j in range(i+1,len(list)):
			for k in range(j+1,len(list)):
				sumlist.append(list[i]+list[j]+list[k])
	for a in range(len(sumlist)):
		if sumlist[a]<=Max:
			blackjack.append(sumlist[a])
	print(max(blackjack))
