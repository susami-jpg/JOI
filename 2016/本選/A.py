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
    
N, M, K = map(int, input().split())
A = [0] + [int(input()) for _ in range(N)]

seg_max = [[-INF] * (N+2) for _ in range(N+2)]
seg_min = [[INF] * (N+2) for _ in range(N+2)]
for l in range(1, N+2):
    for r in range(l+1, min(l+M+1, N+2)):
        if l == r-1:
            seg_max[l][r] = A[l]
            seg_min[l][r] = A[l]
        else:
            seg_max[l][r] = max(seg_max[l][r-1], A[r-1])
            seg_min[l][r] = min(seg_min[l][r-1], A[r-1])
            
dp = [INF] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in range(max(0, i-M), i):
        dp[i] = min(dp[i], dp[j] + K + (i-j)*(seg_max[j+1][i+1] - seg_min[j+1][i+1]))
print(dp[N])

