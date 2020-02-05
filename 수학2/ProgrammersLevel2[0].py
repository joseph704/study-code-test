def solution(n):
    answer=bin(n)
    count1 = 0
    count2 = 0
    result = 0
    for i in answer:
        if i=='1':
            count1+=1

    for j in range(n+1,1000001):
        for k in bin(j):
            if k=='1':
                count2+=1
        if count1==count2:
            result = j
            break
        count2=0
    return result
