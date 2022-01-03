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

N, K = map(int, input().split())
G = [[] for _ in range(10)]
for _ in range(N):
    p, g = map(int, input().split())
    g -= 1
    G[g].append(p)

for i in range(10):
    G[i].sort(reverse=True)
    G[i] = [0] + G[i]
    for j in range(1, len(G[i])):
        G[i][j] += G[i][j-1]
    for j in range(1, len(G[i])):
        G[i][j] += (j-1)*j

dp = [[-INF] * (K+1) for _ in range(11)]
dp[0][0] = 0
for i in range(10):
    for j in range(K+1):
        if dp[i][j] == -INF:continue
        for j2 in range(len(G[i])):
            if j+j2 <= K:
                dp[i+1][j+j2] = max(dp[i+1][j+j2], dp[i][j] + G[i][j2])
print(dp[-1][K])

"""
7 4 
14 1
13 2
12 3
14 2
8 2
16 3
11 2
"""