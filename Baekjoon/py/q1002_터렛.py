'''
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.

조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

'''
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    d = (x2-x1)**2 + (y2-y1)**2
    rr1 = (r1+r2)**2 
    rr2 = (r1-r2)**2
    if x1==x2 and y1==y2:       #동일한 원점
        if r1==r2:
            print(-1)
        else :
            print(0)
    elif r1*r1 > d or r2*r2>d:  #다른원 안에 원점 위치
        if rr2 == d:
            print(1)
        elif rr2 < d:
            print(2)
        else:
            print(0)
    else :
        if rr1 == d:
            print(1)
        elif rr1>d:
            print(2)
        else:
            print(0)