'''
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
'''
import sys
N=int(sys.stdin.readline().rstrip())
word_array = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if word not in word_array:
        word_array.append(word)

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
    tmp_array=[]
    idx_left=0
    idx_right=0
    while idx_left<len(left) and idx_right<len(right):
        if len(left[idx_left])<len(right[idx_right]):
            tmp_array.append(left[idx_left])
            idx_left+=1
        elif len(left[idx_left])>len(right[idx_right]):
            tmp_array.append(right[idx_right])
            idx_right+=1
        else:
            if left[idx_left]<right[idx_right]:
                tmp_array.append(left[idx_left])
                idx_left+=1
            else:
                tmp_array.append(right[idx_right])
                idx_right+=1
    while idx_left<len(left):
        tmp_array.append(left[idx_left])
        idx_left+=1
    while idx_right<len(right):
        tmp_array.append(right[idx_right])
        idx_right+=1
    return tmp_array

sorted_array = merge_sort(word_array)
for word_ in sorted_array:
    print(word_)