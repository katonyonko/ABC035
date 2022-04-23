import io
import sys

_INPUT = """\
6
5 4
1 4
2 5
3 3
1 5
20 8
1 8
4 13
8 8
3 18
5 20
19 20
2 7
4 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import accumulate
  N,Q=map(int,input().split())
  a=[0]*(N+1)
  for i in range(Q):
    l,r=map(int,input().split())
    a[l-1]+=1
    a[r]-=1
  a=list(accumulate(a))
  print(*[a[i]%2 for i in range(N)],sep='')