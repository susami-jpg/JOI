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
S = list(input())
for i in range(N):
    if S[i] == "J":
        S[i] = 0
    elif S[i] == "O":
        S[i] = 1
    else:
        S[i] = 2
        
dp = [[0] * (1<<3) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(1<<3):
        if dp[i][j] == 0:continue
        dp[i+1][j] += dp[i][j]
        lim = -1
        for k in range(3):
            if j&(1<<k):
                lim = k
        if lim < S[i]:
            dp[i+1][j|(1<<S[i])] += dp[i][j]

JOI = dp[N][-1]
JO = dp[N][3]
OI = dp[N][6]
ans = max(JOI+JO, JOI+OI)
for i in range(N):
    ans = max(ans, JOI + dp[i][1] * (dp[N][4] - dp[i][4]))
print(ans)

