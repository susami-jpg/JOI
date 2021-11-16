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
MOD = 10**9+7

setrecursionlimit(10**7)
N = int(input())
A = [int(input()) for _ in range(N)]
A *= 2

#dfsはTLE
"""
dp = dict()
def dfs(l, r):
    if (l, r) in dp:
        return dp[(l, r)]
    if l > r:
        return 0
    if l == r:
        dp[((l, r))] = 0
        return A[l]
    res = 0
    if A[l+1] > A[r]:
        res = max(res, dfs(l+2, r) + A[l])
    else:
        res = max(res, dfs(l+1, r-1) + A[l])
    if A[r-1] > A[l]:
        res = max(res, dfs(l, r-2) + A[r])
    else:
        res = max(res, dfs(l+1, r-1) + A[r])
    dp[(l, r)] = res
    return res
"""

dp = [[0] * 2*N for _ in range(2*N)]
for i in range(2*N):
    dp[i][i] = A[i]

for diff in range(1, 2*N):
    for l in range(2*N-diff):
        r = l+diff
        if A[l+1] > A[r]:
            dp[l][r] = max(dp[l][r], dp[l+2][r] + A[l])
        else:
            dp[l][r] = max(dp[l][r], dp[l+1][r-1] + A[l])
        if A[r-1] > A[l]:
            dp[l][r] = max(dp[l][r], dp[l][r-2] + A[r])
        else:
            dp[l][r] = max(dp[l][r], dp[l+1][r-1] + A[r])
ans = 0
for l in range(N):
    r = l+N-1
    ans = max(ans, dp[l][r])
    #print(l, r, dp[(l, r)])
print(ans)
