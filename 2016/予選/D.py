from sys import exit, stdin, setrecursionlimit
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from itertools import permutations, combinations, accumulate
from math import sqrt, factorial
from decimal import Decimal
#decimalには文字列で渡す PyPyは遅いのでPython3で提出する
#d1 = Decimal('1.1') d2 = Decimal('2.3') -> d1 + d2などの演算で浮動小数点数での誤差がなくなる(割り算もok)
INF = 10**20
MOD = 10**9+7
setrecursionlimit(10**7)
eps = 0.0000000001
#input = stdin.readline

N, T, Q = map(int, input().split())
kingdom = []
person = dict()
for i in range(N):
    a, d = map(int, input().split())
    person[i+1] = (a, d)
    kingdom.append((a, d, i))
kingdom.sort()
stop = [-INF, INF]
pd = -1
pa = -INF
ans = [0] * N
for a, d, i in kingdom:
    if pd == 1 and d == 2:
        diff = abs(pa-a)//2
        ans[i-1] = min(pa+diff, pa+T)
        stop.append(ans[i-1])
        ans[i] = max(a-diff, a-T)
        stop.append(ans[i])
    pd = d
    pa = a
stop.sort()
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)
def OrMore(K: int, A: list) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)
for a, d, i in kingdom:
    if d == 1:
        _, ind = OrMore(a, stop)
        y = stop[ind]
        ans[i] = min(a+T, y)
    else:
        _, ind = OrLessThan(a, stop)
        y = stop[ind]
        ans[i] = max(a-T, y)

for _ in range(Q):
    x = int(input())
    x -= 1
    print(ans[x])




