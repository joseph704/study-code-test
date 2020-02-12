N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]

arr = []


def dfs(cnt):
    if (cnt == M):
        print(*arr)
        return

    for i in range(0, N):


        arr.append(num_list[i])
        dfs(cnt + 1)
        arr.pop()

dfs(0)