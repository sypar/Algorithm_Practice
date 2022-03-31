'''
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
'''
import sys
px = [0]*3
py = [0]*3
for idx in range(3):
    px[idx],py[idx] = map(int,sys.stdin.readline().split())

def find_coord(p):
    for idx in range(3):
        point = p[idx]
        p[idx]=0
        if point in p:
            p[idx]=point
        else :
            return point

print(f'{find_coord(px)} {find_coord(py)}')