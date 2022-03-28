import sys
import math
M=int(sys.stdin.readline().rstrip())
N=int(sys.stdin.readline().rstrip())
data = []
for val in range(M,N+1):
    if val>5:
        for dec in range(2,math.floor(math.sqrt(val))+1):
            if val%dec == 0:
                break
            elif dec==math.floor(math.sqrt(val)):
                data.append(val)
    else : # val<=5
        if val in [2,3,5]:
            data.append(val)
if data!=[]:
    print(f'{sum(data)}\n{data[0]}')
else : #empty
    print(-1)