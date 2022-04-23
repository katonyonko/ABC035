import io
import sys

_INPUT = """\
6
UL?
1
UD?
1
UUUU?DDR?LLLL
1
UULL?
2
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=int(input())
  x,y=0,0
  z=0
  for i in range(len(S)):
    if S[i]=='L': x-=1
    elif S[i]=='R': x+=1
    elif S[i]=='D': y-=1
    elif S[i]=='U': y+=1
    else: z+=1
  if T==1: print(abs(x)+abs(y)+z)
  else:
    if abs(x)+abs(y)-z>=0: print(abs(x)+abs(y)-z)
    else: print((abs(x)+abs(y)-z)%2)