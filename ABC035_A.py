import io
import sys

_INPUT = """\
6
4 3
16 9
28 21
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  W,H=map(int,input().split())
  if W//4*3==H: print('4:3')
  else: print('16:9')