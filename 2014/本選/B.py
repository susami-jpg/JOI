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

m, n = map(int, input().split())
a = [int(input()) for _ in range(m)]
a.sort(reverse=True)
a = list(accumulate([0] + a))
boxes = [tuple(map(int, input().split())) for _ in range(n)]
dp = [-INF] * (m+1)
dp[0] = 0
for i in range(n):
    p = [-INF] * (m+1)
    p, dp = dp, p
    for j in range(m+1):
        if p[j] == -INF:continue
        dp[j] = max(dp[j], p[j])
        c, e = boxes[i]
        rest = min(j+c, m)
        dp[rest] = max(dp[rest], p[j] + a[rest]-a[j] - e)
print(max(dp))

    
