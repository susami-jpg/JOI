from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

N, M, X = map(int, input().split())
H = [int(input()) for _ in range(N)]
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    edge[a-1].append((b-1, t))
    edge[b-1].append((a-1, t))

def dijkstra(s, g):
    dist = [INF] * N
    fix = [False] * N
    hq = [(0, s)]
    dist[s] = 0
    while hq:
        _, v = heappop(hq)
        fix[v] = True
        h_now = max(0, X-dist[v])
        h_now = min(h_now, H[v])
        for nextv, cost in edge[v]:
            if fix[nextv]:continue
            if H[v] - cost < 0:continue
            if H[nextv] + cost < h_now:
                cost += h_now - (H[nextv] + cost)
            elif cost > h_now:
                cost += cost - h_now
            if dist[nextv] > dist[v] + cost:
                dist[nextv] = dist[v] + cost
                heappush(hq, (dist[nextv], nextv))
    #print(dist)
    h_now = max(0, X-dist[g])
    h_now = min(h_now, H[g])
    dist[g] += H[g] - h_now
    return dist[g]

ans = dijkstra(0, N-1)
if ans >= INF:
    print(-1)
else:
    print(ans)

