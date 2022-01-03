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
MOD = 10007
setrecursionlimit(10**7)
eps = 0.0000000001
input = stdin.readline

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
dp[0][1] = 1
for i in range(N):
    for s in range(1<<3):
        if dp[i][s] == 0:continue
        for nxts in range(1<<3):
            if (nxts>>S[i])&1 == 0:
                continue
            if (nxts&s) == 0:continue
            dp[i+1][nxts] += dp[i][s]
            dp[i+1][nxts] %= MOD
print(sum(dp[N])%MOD)
 
        