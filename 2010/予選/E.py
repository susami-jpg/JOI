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
MOD = 100000
setrecursionlimit(10**7)

W, H = map(int, input().split())
dp = [[[[0] * 2 for _ in range(2)] for _ in range(W)] for _ in range(H)]
dp[1][0][0][0] = dp[0][1][1][0] = 1

for i in range(H):
    for j in range(W):
        for k in range(2):
            for l in range(2):
                if dp[i][j][k][l] == 0:continue
                if i+1 < H:
                    if k == 0 and l == 0:
                        dp[i+1][j][0][0] += dp[i][j][k][l]
                        dp[i+1][j][0][0] %= MOD
                    if k == 1 and l == 0:
                        dp[i+1][j][0][1] += dp[i][j][k][l]
                        dp[i+1][j][0][1] %= MOD
                    if k == 0 and l == 1:
                        dp[i+1][j][0][0] += dp[i][j][k][l]
                        dp[i+1][j][0][0] %= MOD
                if j+1 < W:
                    if k == 1 and l == 0:
                        dp[i][j+1][1][0] += dp[i][j][k][l]
                        dp[i][j+1][1][0] %= MOD
                    if k == 0 and l == 0:
                        dp[i][j+1][1][1] += dp[i][j][k][l]
                        dp[i][j+1][1][1] %= MOD
                    if k == 1 and l == 1:
                        dp[i][j+1][1][0] += dp[i][j][k][l]
                        dp[i][j+1][1][0] %= MOD
ans = 0
for k in range(2):
    for l in range(2):
        ans += dp[H-1][W-1][k][l]
        ans %= MOD
print(ans)




