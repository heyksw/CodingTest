'''
# 6-1 선택 정렬 (selection sort)
array = [7,5,9,0,8,3,1,6,2,4]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index=j
      
  array[min_index], array[i] = array[i], array[min_index]

print(array)


# 6-2 삽입 정렬 (insertion sort)
array = [7,5,9,0,8,3,1,6,2,4]

for i in range(1, len(array)):
  sorted_index = i
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break
print(array)

# 6-3 퀵 정렬 (quick sort)
array = [7,5,9,0,8,3,1,6,2,4]

def quick_sort(array,start,end):
  if start >= end: # 원소가 1개일 경우 재귀 종료
    return 
  pivot = start
  left = start+1
  right = end 
  while left <= right:
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] <= array[pivot]:
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복 
    while right >= start and array[right] >= array[pivot]:
      right -=1 
    # 엇갈렸다면 작은 데이터와 피벗을 교체 
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
    else :
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array,start,right-1)
  quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)

# 6-5 파이썬의 장점을 살린 퀵 정렬 
# (quick sort with Python's advantages)
array = [7,5,9,0,8,3,1,6,2,4]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array)<=1:
    return array
  
  pivot = array[0] # 피벗은 첫 번째 원소
  tail = array[1:] # 피벗을 제외한 리스트 

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 선택 정렬 복습 (selection sort)
array = [7,5,9,0,8,3,1,6,2,4]

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index=j
  array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입 정렬 복습 (insertion sort)
array = [7,5,9,0,8,3,1,6,2,4]

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1] :
      array[j], array[j-1] = array[j-1], array[j]
    else :
      break
print(array)


# 계수 정렬 (count sort)
# 모든 원소의 값이 0보다 크거나 같다고 가정
array= [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0]*(max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):
  for j in range(count[i]):
    print(i,end=' ')
print()

# using python sort library 1
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

# using python sort library 2
array = [7,5,9,0,3,1,6,2,4,8]

array.sort()  
print(array)

# using key
array = [('바나나',2),('사과',5),('당근',3)]
def setting(data):
  return data[1]
result = sorted(array, key = setting)
print(result)


# 2. 위에서 아래로
n = int(input())
array = []
for _ in range(n):
  array.append(int(input()))

array.sort(reverse = True)
print(array)

#3 성적이 높은 순서로 학생 출력하기
n = int(input())
list = []
for _ in range(n):
  input_data = input().split() 
  list.append((input_data[0],int(input_data[1])))

def keyFunc(data):
  return data[1] 

list.sort(key = keyFunc, reverse = True)

print(list)
  
'''

# 4 두 배열의 원소 교체
n, k = map(int,input().split())

arrayA=list(map(int,input().split()))
arrayB=list(map(int,input().split()))

for _ in range(k):
  minA = min(arrayA)
  minA_idx = arrayA.index(minA)
  maxB = max(arrayB)
  maxB_idx = arrayB.index(maxB)

  arrayA[minA_idx], arrayB[maxB_idx] = arrayB[maxB_idx], arrayA[minA_idx]

print(sum(arrayA))
