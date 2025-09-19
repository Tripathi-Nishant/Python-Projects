import sys
sys.setrecursionlimit(10000)

def worth(s):
    return sum(ord(c) - ord('a') + 1 for c in s)

def solve():
    N, M = map(int, input().split())
    strings = input().split()
    costs = list(map(int, input().split()))
    worths = [worth(s) for s in strings]

    idx = {s: i for i, s in enumerate(strings)}
    conflict = [[] for _ in range(N)]
    for _ in range(M):
        a, b = input().split()
        i, j = idx[a], idx[b]
        conflict[i].append(j)
        conflict[j].append(i)

    budget = int(input())
    best = 0
    chosen = [False]*N

    def dfs(i, used, value):
        nonlocal best
        if used > budget:
            return
        if i == N:
            best = max(best, value)
            return
        # skip i
        dfs(i+1, used, value)

        # try take i
        can = True
        for j in conflict[i]:
            if chosen[j]:  # conflict detected
                can = False
                break
        if can and used + costs[i] <= budget:
            chosen[i] = True
            dfs(i+1, used + costs[i], value + worths[i])
            chosen[i] = False

    dfs(0, 0, 0)
    print(best, end="")

if __name__ == "__main__":
    solve()
