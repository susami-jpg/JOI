from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]
clothing = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-INF] * N for _ in range(D)]
for j in range(N):
    a, b, c = clothing[j]
    if a <= T[0] <= b:
        dp[0][j] = 0

for i in range(1, D):
    t = T[i]
    for j in range(N):
        a1, b1, c1 = clothing[j]
        if a1 <= t <= b1:
            for k in range(N):
                a0, b0, c0 = clothing[k]
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(c1-c0))
print(max(dp[D-1]))

                