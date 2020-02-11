N, M = map(int, input().split())

num_list = [i + 1 for i in range(N)]
check_list = [False] * N

arr = []


def dfs(cnt):
    if (cnt == M):
        print(*arr)
        return

    for i in range(0, N):
        if (check_list[i]):
            continue

        check_list[i] = True
        arr.append(num_list[i])
        dfs(cnt + 1)
        arr.pop()

        # 이 부분이 순열하고의 차이점이다.
        # 큰 나무에서 전에 봤던 것만
        # 닫아주면 된다.
        for j in range(i + 1, N):
            check_list[j] = False


dfs(0)