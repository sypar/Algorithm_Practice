'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
import sys
T=int(sys.stdin.readline().rstrip())
arr = [0 for _ in range(T)]
for idx in range(T):
    arr[idx]=int(sys.stdin.readline().rstrip())

def qsort(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    n_arr = array[1:]
    
    left = [ x for x in n_arr if x<=pivot]
    right = [ x for x in n_arr if x>=pivot]
    
    return qsort(left) + [pivot] + qsort(right)

def mergesort(array):
    if len(array)<=1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    left = mergesort(left)
    right = mergesort(right)
    return merge_(left,right)

def merge_(left,right):
    tmp_array = []
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            tmp_array.append(left[i])
            i+=1
        else:
            tmp_array.append(right[j])
            j+=1
    while i<len(left):
        tmp_array.append(left[i])
        i+=1
    while j<len(right):
        tmp_array.append(right[j])
        j+=1
    return tmp_array

arr = mergesort(arr)
for idx in range(T):
    print(arr[idx])