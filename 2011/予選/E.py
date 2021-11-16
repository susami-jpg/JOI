from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt
from copy import copy, deepcopy
INF = 10**15
MOD = 10**9+7

H, W, N = map(int, input().split())
maze = [input() for _ in range(H)]
plants = [0] * N
for i in range(H):
    for j in range(W):
        if maze[i][j] == "." or maze[i][j] == "X":
            continue
        elif maze[i][j] == "S":
            sy, sx = i, j
        else:
            plants[int(maze[i][j])-1] = (i, j)

plants = [(sy, sx)] + plants

def valid(y, x):
    return 0<=y<H and 0<=x<W and maze[y][x] != "X"

def bfs(sy, sx, gy, gx):
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    deq = deque()
    deq.append((sy, sx))
    dist = [[INF] * W for _ in range(H)]
    dist[sy][sx] = 0
    while deq:
        y, x = deq.popleft()
        if y == gy and x == gx:
            break
        for i in range(4):
            nexty = y+dy[i]
            nextx = x+dx[i]
            if not valid(nexty, nextx):continue
            if dist[nexty][nextx] != INF:continue
            dist[nexty][nextx] = dist[y][x] + 1
            deq.append((nexty, nextx))  
    return dist[gy][gx]

ans = 0
for i in range(N):
    sy, sx = plants[i]
    gy, gx = plants[i+1]
    ans += bfs(sy, sx, gy, gx)
print(ans)
