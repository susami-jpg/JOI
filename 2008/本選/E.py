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

W, H = map(int, input().split())
w_set = set()
h_set = set()
N = int(input())
msks = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    msks.append((x1, y1, x2, y2))
    w_set.add(x1)
    w_set.add(x1+1)
    w_set.add(x2)
    w_set.add(x2+1)
    h_set.add(y1)
    h_set.add(y1+1)
    h_set.add(y2)
    h_set.add(y2+1)

w_set.add(0)
w_set.add(W)
h_set.add(0)
h_set.add(H)

def CC(A: list) -> list:
    '座標圧縮'
    #index -> 実際の値のdict
    B = {}
    #実際の値 -> indexのdict
    C = {}
    for i, j in enumerate(sorted(set(A))):
        B[i] = j
        C[j] = i
    return B, C

ind_to_w, w_to_ind = CC(w_set)
ind_to_h, h_to_ind = CC(h_set)

cW = len(ind_to_w)
cH = len(ind_to_h)
field = [[0]*cW for _ in range(cH)]
for x1, y1, x2, y2 in msks:
    x1 = w_to_ind[x1]
    y1 = h_to_ind[y1]
    x2 = w_to_ind[x2]
    y2 = h_to_ind[y2]
    field[y1][x1] += 1
    field[y2][x2] += 1
    field[y1][x2] -= 1
    field[y2][x1] -= 1

for i in range(cH):
    for j in range(1, cW):
        field[i][j] += field[i][j-1]

for i in range(1, cH):
    for j in range(cW):
        field[i][j] += field[i-1][j]

new_field = []
#端っこの含む含まない判定が難しい
#とりあえず、サンプルで確認してみて調整するのが早い
for i in range(h_to_ind[H]):
    new_field.append(field[i][:w_to_ind[W]])

new_field, field = field, new_field

cH = len(field)
cW = len(field[0])
dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
seen = [[0]*cW for _ in range(cH)]
def valid(y, x):
    return 0 <= y < cH and 0 <= x < cW and field[y][x] == 0 and seen[y][x] == 0

ans = 0
def bfs(sy, sx):
    global ans
    deq = deque()
    deq.append((sy, sx))
    seen[sy][sx] = 1
    while deq:
        y, x = deq.popleft()
        for a, b in dxdy:
            nxty = y+a
            nxtx = x+b
            if valid(nxty, nxtx):
                seen[nxty][nxtx] = 1
                deq.append((nxty, nxtx))
    ans += 1
    return

for i in range(cH):
    for j in range(cW):
        if field[i][j]:
            field[i][j] = 1
        if valid(i, j):
            bfs(i, j)

print(ans)
