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

N = int(input()) + 1
S = " " + input()
J = [0] * N
O = [0] * N
I = [0] * N
for i in range(1, N):
    if S[i] == "J":
        J[i] += 1
    elif S[i] == "O":
        O[i] += 1
    else:
        I[i] += 1

J = list(accumulate(J))
O = list(accumulate(O))
I = list(accumulate(I))
JO = [0] * N
JI = [0] * N
for i in range(N):
    JO[i] = J[i] - O[i]
    JI[i] = J[i] - I[i]

ans = 0
rec = defaultdict(list)
for i in range(N):
    rec[(JO[i], JI[i])].append(i)

for _, L in rec.items():
    ma = max(L)
    mi = min(L)
    ans = max(ans, ma-mi)
print(ans)


        