from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**15
MOD = 10000 

N, K = map(int, input().split())
menu = [0] * (N+1)
for _ in range(K):
    a, b = map(int, input().split())
    menu[a] = b

dp = [[[0] * 4 for _ in range(4)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(4):
        for k in range(4):
            if dp[i][j][k] == 0:continue
            if menu[i+1] != 0:
                l = menu[i+1]
                if l == j == k:continue
                dp[i+1][l][j] += dp[i][j][k]
                dp[i+1][l][j] %= MOD
            else:
                for l in range(1, 4):
                    if l == j == k:continue
                    dp[i+1][l][j] += dp[i][j][k]
                    dp[i+1][l][j] %= MOD
ans = 0
for j in range(1, 4):
    for k in range(1, 4):
        ans += dp[N][j][k]
        ans %= MOD
print(ans)
         
                
