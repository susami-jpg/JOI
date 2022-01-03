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

N, M = map(int, input().split())
x_plots = []
y_plots = []
for _ in range(M):
    x, y = map(int, input().split())
    x_plots.append(x)
    y_plots.append(y)
x_plots.sort()
y_plots.sort()

ng = -1
ok = INF

def is_ok(x):
    cur = -1
    cnt = 0
    for i in range(M):
        if cur < x_plots[i]:
            cur = x_plots[i]+x
            cnt += 1
    cur = -1
    for i in range(M):
        if cur < y_plots[i]:
            cur = y_plots[i]+x
            cnt += 1
    if cnt <= N:
        return True
    else:
        return False

        
while abs(ng-ok) > 1:
    mid = (ok+ng)//2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid


print(ok)

    