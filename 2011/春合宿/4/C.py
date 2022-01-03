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
input = stdin.readline

K, N, M = map(int, input().split())
lim_rank = -(-K//12)
ruck_scores = []
bad_scores = []
scores = []
for _ in range(K):
    p = int(input())
    scores.append(p)
    ruck_scores.append(p + (N-M)*100)
    bad_scores.append(p)

ruck_scores.sort()
bad_scores.sort()
fix = []
prob = []

def OrMore(K: int, A: list, l) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    return l - ans, (ans if ans <= l - 1 else -1)

for i in range(K):
    k, _ = OrMore(scores[i] + 1, ruck_scores, K)
    if N-M == 0:
        e = 0
    else:
        e = 1
    if k < lim_rank+e:
        fix.append(i+1)
    k, _ = OrMore(scores[i] + (N-M)*100 + 1, bad_scores, K)
    if k < lim_rank:
        prob.append(i+1)

for a in fix:
    print(a)
print("-" * 8)
for a in prob:
    print(a)
    