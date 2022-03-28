# Input : N ( 0 <= A,B <= 10E+10000 )
# Output 

import sys
A,B = map(str,sys.stdin.readline().split())
pSUM = 0
sSUM = ""

while len(A)!=len(B):
    if len(A)>len(B):
        B='0'+ B
    else:
        A='0'+ A

for idx in range(-1,-len(A)-1,-1):
    pSUM += int(A[idx]) + int(B[idx])
    if pSUM <10:
        sSUM = str(pSUM) + sSUM
        pSUM = 0 #init
    else : # 10 <= pSUM < 20
        sSUM = str(pSUM%10) + sSUM
        pSUM = 1

if pSUM != 0:
    print(str(pSUM)+sSUM)
else :
    print(sSUM)
# Python은 sys.maxsize의 값이더라도, 더하여 자료에 저장가능하다.
# C나 C++ 인 경우 위와같이 프로그래밍하면된다.