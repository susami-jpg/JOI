from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)
eps = 0.0000000001
#input = stdin.readline

N = int(input())
M = int(input())
D = int(input())
K = int(input())
plots = []
for i in range(N):
    x, y = map(int, input().split())
    plots.append((x, y, i))
plots.sort()
edge = [[] for _ in range(N)]
deq = deque()
r = 0
for l in range(N):
    x, y, i = plots[l]
    while deq:
        if abs(x-deq[0][0]) > D:
            deq.popleft()
        else:
            break
    while r < N:
        if abs(x-plots[r][0]) <= D:
            deq.append(plots[r])
            r += 1
        else:
            break
    for nx, ny, ni in deq:
        if abs(nx-x)**2 + abs(ny-y)**2 <= D**2:
            edge[i].append(ni)
            edge[ni].append(i)

dp = [-INF]*N
dp[0] = 1
for _ in range(K):
    p = [-INF]*N
    p, dp = dp, p
    for j in range(N):
        if p[j] == -INF:continue
        dp[j] = p[j]+1
        for j2 in edge[j]:
            dp[j2] = max(p[j2]+1, 1)
    

ans = 0
for j in range(N):
    if 1 <= dp[j] <= M:
        ans += 1
print(ans)


   
        