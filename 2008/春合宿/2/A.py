from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**10
MOD = 10**9+7
setrecursionlimit(10**7)

N, D = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(D)]
dp = [[INF] * N for _ in range(3)]
for j in range(N):
    dp[0][j] = cost[0][j]

for i in range(1, D):
    p = [[INF] * N for _ in range(3)]
    p, dp = dp, p
    comp = [INF] * N
    for j in range(N):
        comp[j] = min(p[0][j], p[1][j], p[2][j])
    left = [INF] + comp
    right = comp + [INF]
    for j in range(N):
        left[j+1] = min(left[j+1], left[j])
        right[N-j-1] = min(right[N-j-1], right[N-j])
    for j in range(N):
        dp[0][j] = min(left[j], right[j+1]) + cost[i][j]
        dp[1][j] = p[0][j] + (cost[i][j] * 9)//10
        dp[2][j] = min(p[1][j], p[2][j]) + (cost[i][j] * 7)//10

ans = min(min(dp[0]), min(dp[1]), min(dp[2]))
print(ans)

N, D = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(D)]
dp = [[INF] * N for _ in range(3)]
for j in range(N):
    dp[0][j] = cost[0][j]

for i in range(1, D):
    p = [[INF] * N for _ in range(3)]
    p, dp = dp, p
    vmin = INF
    for j in range(N):
        vmin = min(vmin, p[0][j], p[1][j], p[2][j])
    for j in range(N):
        dp[0][j] = vmin + cost[i][j]
        dp[1][j] = p[0][j] + (cost[i][j] * 9)//10
        dp[2][j] = min(p[1][j], p[2][j]) + (cost[i][j] * 7)//10

ans = min(min(dp[0]), min(dp[1]), min(dp[2]))
print(ans)

"""
4 5
110 160 80 200
150 170 80 120
80 150 160 160
160 110 200 110
150 190 160 190
"""
