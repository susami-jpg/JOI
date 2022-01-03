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
def main():
    input = stdin.readline
    N, T, S = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    dp_prev = [[0] * (S+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(S+1):
            dp_prev[i+1][j] = max(dp_prev[i+1][j], dp_prev[i][j])
            nxtj = j+B[i]
            if nxtj > S:continue
            dp_prev[i+1][nxtj] = max(dp_prev[i+1][nxtj], dp_prev[i][j] + A[i])
                

    dp_after = [[0] * (T-S+1) for _ in range(N+1)]
    for i in range(N, 0, -1):
        for j in range(T-S+1):
            dp_after[i-1][j] = max(dp_after[i-1][j], dp_after[i][j])
            nxtj = j+B[i-1]
            if nxtj > T-S:continue
            dp_after[i-1][nxtj] = max(dp_after[i-1][nxtj], dp_after[i][j] + A[i-1])

    ans = 0
    for i in range(N+1):
        ans = max(ans, dp_prev[i][S] + dp_after[i][T-S])
    print(ans)

if __name__ == "__main__":
    main()
    