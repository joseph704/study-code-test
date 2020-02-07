import sys
from collections import Counter

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    list.append(int(sys.stdin.readline()))
print(round(sum(list)/n))

if n==1:
    print(list[0])
    print(list[0])
    print(0)
    sys.exit()

list.sort()
print(list[len(list)//2])
cnt = Counter(list)
cnt = cnt.most_common()

if cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(list[-1]-list[0])