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

def OrMore(K: int, A: list) -> int:
    '配列Aの中のうち、k以上の個数と始まりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_left(A, K)
    l = len(A)
    return l - ans, (ans if ans <= l - 1 else -1)
def OrLessThan(K: int, A: list) -> int:
    '配列Aの中のうち、k以下の個数と終わりの0indexを返すライブラリ'
    '-1の時は解が無い時'
    ans = bisect_right(A, K)
    return ans, (-1 if ans == 0 else ans - 1)

N, K = map(int, input().split())
S = input()
J = [0] * N
O = [0] * N
I = [0] * N
for i in range(N):
    if S[i] == "J":
        J[i] = 1
    elif S[i] == "O":
        O[i] = 1
    else:
        I[i] = 1
J = list(accumulate(J))
O = list(accumulate(O))
I = list(accumulate(I))

ans = INF
for l in range(N):
    cnt_J = J[l]
    if cnt_J < K:continue
    cur_O = O[l]
    k, r = OrMore(cur_O+K, O)
    if r == -1:continue
    if I[-1]-I[r] < K:continue
    cnd = N-3*K
    k, _ = OrLessThan(J[l]-K, J)
    cnd -= k
    k, _ = OrMore(I[r]+K, I)
    cnd -= (k-1)
    ans = min(ans, cnd)
if ans == INF:
    print(-1)
else:
    print(ans)
    




    