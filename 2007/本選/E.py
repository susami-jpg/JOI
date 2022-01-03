from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial, gcd
from decimal import Decimal
from functools import reduce
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**18
MOD = 10**9+7
setrecursionlimit(10**7)
eps = 0.0000000001
#input = stdin.readline
def lcm(x, y):
    return (x * y) // gcd(x, y)

def lcm_2(*vals):
    return reduce(lcm, vals)
N = int(input())
left_child = [-1] * N
right_child = [-1] * N
left = [0] * N
right = [0] * N
par = [-1] * N
for v in range(N):
    l, r, lc, rc = map(int, input().split())
    left[v] = l
    right[v] = r
    lc -= 1
    rc -= 1
    left_child[v] = lc
    right_child[v] = rc
    if lc != -1:
        par[lc] = v
    if rc != -1:
        par[rc] = v

p = 0
while par[p] != -1:
    p = par[p]

right_weight = [-1] * N
left_weight = [-1] * N
seg_weight = [-1] * N
def dfs(v, par=-1):
    lc = left_child[v]
    rc = right_child[v]
    if lc == -1 and rc == -1:
        x = left[v]
        y = right[v]
        l = lcm_2(*[x, y])
        right_weight[v] = l//x
        left_weight[v] = l//y
        seg_weight[v] = right_weight[v] + left_weight[v]
        return seg_weight[v]
    elif lc == -1:
        if right_weight[v] == -1:
            dfs(right_child[v], v)
        Wy = seg_weight[rc]
        right_weight[v] = Wy
        x = left[v]
        y = right[v]
        l = lcm_2(*[x, y*Wy])
        left_weight[v] = l//x
        right_weight[v] = l//y
        seg_weight[v] = left_weight[v] + right_weight[v]
    elif rc == -1:
        if left_weight[v] == -1:
            dfs(left_child[v], v)
        Wx = seg_weight[lc]
        left_weight[v] = Wx
        x = left[v]
        y = right[v]
        l = lcm_2(*[y, x*Wx])
        right_weight[v] = l//y
        left_weight[v] = l//x
        seg_weight[v] = left_weight[v] + right_weight[v]
    else:
        if left_weight[v] == -1:
            dfs(left_child[v], v)
        if right_weight[v] == -1:
            dfs(right_child[v], v)
        x = left[v]
        y = right[v]
        Wx = seg_weight[lc]
        Wy = seg_weight[rc]
        left_weight[v] = Wx
        right_weight[v] = Wy
        l = lcm_2(*[x*Wx, y*Wy])
        left_weight[v] = l//x
        right_weight[v] = l//y
        seg_weight[v] = left_weight[v] + right_weight[v]
    return

dfs(p)
print(seg_weight[p])
