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

P = int(input())
N = int(input())
N %= (P-1)
rec = defaultdict(int)
for x in range(P):
    rec[pow(x, N, P)] += 1

keys = set()
for key in range(P):
    if rec[key]:
        keys.add(key)

ans = 0
for x in keys:
    for y in keys:
        z = (x+y)%P
        ans += rec[x]*rec[y]*rec[z]
print(ans)

    