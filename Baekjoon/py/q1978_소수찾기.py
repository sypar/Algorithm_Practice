#input 0<N<100
import sys
import math

N = int(sys.stdin.readline().rstrip())
data = list(map(int,sys.stdin.readline().split()))
cnt = 0
for idx in range(N):
    if data[idx] == 1:
        continue
    elif data[idx] in [2,3,5]:
        cnt+=1
    else :
        for M in range(2,math.floor(math.sqrt(data[idx]))+1):
            if data[idx]%M == 0:
                break
            elif M==math.floor(math.sqrt(data[idx])):
                cnt+=1
print(cnt)