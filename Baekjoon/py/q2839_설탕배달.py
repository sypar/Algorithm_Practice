# Input : N ( 3 <= N <= 5000 )
# Output 
import sys
N = int(sys.stdin.readline().rstrip())
kg5_cnt,remain = divmod(N,5)
kg3_cnt=0
if remain == 1 :
    kg5_cnt-=1
    kg3_cnt+=2
elif remain == 2 :
    kg5_cnt-=2
    kg3_cnt+=4
elif remain == 3 :
    kg3_cnt+=1
elif remain == 4 :
    kg5_cnt-=1
    kg3_cnt+=3
    
if kg5_cnt>=0:
    print(kg3_cnt+kg5_cnt)
else : # kg5_cnt<0
    print(-1)