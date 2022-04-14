'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
python -> 시간초과 / pypy -> 12692ms
'''
import sys
n = int(sys.stdin.readline().rstrip())
plate = [ [ 0 for _ in range(n)] for _ in range(n) ]
y = [ i for i in range(n)]
count=0

def dfs(tx,ty,depth):
    global plate,count
    if depth>=n:
        count+=1
        return
    if depth==0:
        if len(ty)%2 == 0:
            length = len(ty)//2
        else:
            length = (len(ty)//2) +1
    else:
        length = len(ty)
    for idx in range(length):
        if plate[tx][ty[idx]]==0 and visit(tx,ty[idx]):
            plate[tx][ty[idx]]=1
            dfs(tx+1,ty[:idx]+ty[idx+1:],depth+1)
            plate[tx][ty[idx]]=0
        if idx == (len(ty)//2)-1 and depth==0:
            count=count*2

def visit(vx,vy):
    global plate
    sx=[-1,1,1,-1]
    sy=[1,1,-1,-1]
    for i in range(4):
        ix=vx
        iy=vy
        while True:
            ix+=sx[i]
            iy+=sy[i]
            if ix<0 or ix>=n or iy<0 or iy>=n:
                break
            elif plate[ix][iy]==1:
                return 0
    return 1

dfs(0,y,0)
print(count)