from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))

cluster = []
prev = A[0]
cnt = 1
for i in range(N-1):
    if prev == 1-A[i+1]:
        prev = A[i+1]
        cnt += 1
    else:
        cluster.append(cnt)
        cnt = 1
        prev = A[i+1]
cluster.append(cnt)

ans = 0
cluster = [0] + cluster + [0]
L = len(cluster)
for i in range(1, L-1):
    ans = max(ans, cluster[i-1]+cluster[i]+cluster[i+1])
print(ans)

