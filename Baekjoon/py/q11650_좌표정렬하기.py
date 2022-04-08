'''
문제
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

출력
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''
import sys
N=int(sys.stdin.readline().rstrip())
tr = [[0, 0] for _ in range(N)]

for idx in range(N):
    tr[idx] = list(map(int,sys.stdin.readline().split()))

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge_(left,right)

def merge_(left,right):
    tmp_array = []
    l=0
    r=0
    while l<len(left) and r<len(right):
        if left[l][0]<right[r][0]:
            tmp_array +=[left[l]]
            l+=1
        elif left[l][0]>right[r][0]:
            tmp_array += [right[r]]
            r+=1
        elif left[l][0]==right[r][0]:
            if left[l][1]<=right[r][1]:
                tmp_array+=[left[l]]
                l+=1
            else:
                tmp_array+=[right[r]]
                r+=1
    while l<len(left):
        tmp_array+=[left[l]]
        l+=1
    while r<len(right):
        tmp_array+=[right[r]]
        r+=1
    return tmp_array
    
new_tr=merge_sort(tr)
for idx in range(N):
    print(f'{new_tr[idx][0]} {new_tr[idx][1]}')