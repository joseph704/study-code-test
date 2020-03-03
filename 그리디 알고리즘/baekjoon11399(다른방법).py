case_num = int(input())
numlist = list(map(int,input().split()))
check_list = [False] * case_num
arr = []
sumarr = []

def find(cnt):
    if cnt == case_num:
        count = 0
        result = 0
        for j in arr:
            count = count + j
            result += count
        sumarr.append(result)
        return
    for i in range(case_num):
        if check_list[i]:
            continue
        check_list[i] = True
        arr.append(numlist[i])
        find(cnt + 1)

        arr.pop()
        check_list[i] = False
find(0)
print(max(sumarr))