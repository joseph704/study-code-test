N,tot = map(int,input().split())
list=[]
for i in range(N):
    list.append(int(input()))
count = 0
list.reverse()

for j in range(len(list)):
    if tot//list[j]>0:
        count += tot//list[j]
        tot -= list[j]*(tot//list[j])
print(count)