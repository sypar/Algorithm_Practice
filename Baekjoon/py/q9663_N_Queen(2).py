'''
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
python -> 18716ms / pypy -> 3032ms
'''
import sys
n = int(sys.stdin.readline().rstrip())
y = [ i for i in range(n)]
check_sum=[ 0 for _ in range(2*n)]
check_diff=[ 0 for _ in range(2*n)]
count=0

def dfs(tx,ty):
    global plate,count
    if tx>=n:
        count+=1
        return
    if tx==0:
        if len(ty)%2 == 0:
            length = len(ty)//2
        else:
            length = (len(ty)//2) +1
    else:
        length = len(ty)
    for idx in range(length):
        if check_sum[tx+ty[idx]]==1 or check_diff[n+tx-ty[idx]]==1:
            continue
        check_sum[tx+ty[idx]]=1
        check_diff[n+tx-ty[idx]]=1
        dfs(tx+1,ty[:idx]+ty[idx+1:])
        check_sum[tx+ty[idx]]=0
        check_diff[n+tx-ty[idx]]=0
        if idx == (len(ty)//2)-1 and tx==0:
            count=count*2

dfs(0,y)
print(count)