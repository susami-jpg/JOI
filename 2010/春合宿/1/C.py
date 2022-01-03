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
MOD = 1234567
setrecursionlimit(10**7)

N, P = map(int, input().split())
H = [0] + [int(input()) for _ in range(N)]
for i in range(1, N+1):
    H[i] += H[i-1]

def OrMore(K: int, A: list) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)

dp = [0] * (N+1)
acc_dp = [0] * (N+1)
dp[0] = acc_dp[0] = 1

for i in range(1, N+1):
    _, j = OrMore(H[i]-P, H)
    dp[i] = acc_dp[i-1]
    if j-1 >= 0:
        dp[i] -= acc_dp[j-1]
    dp[i] %= MOD
    acc_dp[i] += acc_dp[i-1] + dp[i]
    acc_dp[i] %= MOD
print(dp[N]%MOD)

    
"""
6 350 
315
191
98
70
126
200
"""