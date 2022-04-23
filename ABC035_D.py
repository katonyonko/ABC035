import io
import sys

_INPUT = """\
6
2 2 5
1 3
1 2 2
2 1 1
2 2 3
1 3
1 2 2
2 1 1
8 15 120
1 2 6 16 1 3 11 9
1 8 1
7 3 14
8 2 13
3 5 4
5 7 5
6 4 1
6 8 17
7 8 5
1 4 2
4 7 1
6 1 3
3 1 10
2 6 5
2 4 12
5 1 30
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop,heappush
  def Dijkstra(G,s):
    done=[False]*len(G)
    inf=10**20
    C=[inf]*len(G)
    C[s]=0
    h=[]
    heappush(h,(0,s))
    while h:
      x,y=heappop(h)
      if done[y]:
        continue
      done[y]=True
      for v in G[y]:
        if C[v[1]]>C[y]+v[0]:
          C[v[1]]=C[y]+v[0]
          heappush(h,(C[v[1]],v[1]))
    return C
  N,M,T=map(int,input().split())
  A=list(map(int,input().split()))
  G1=[[] for _ in range(N)]
  G2=[[] for _ in range(N)]
  for i in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    G1[a].append((c,b))
    G2[b].append((c,a))
  C1=Dijkstra(G1,0)
  C2=Dijkstra(G2,0)
  ans=0
  for i in range(N):
    if C1[i]+C2[i]<=T: ans=max(ans,A[i]*(T-C1[i]-C2[i]))
  print(ans)