# 파이썬에서 리스트 복사는 a = b[:] 슬라이싱으로 이루어져야 한다 !
# 파이썬에서 
listA = [1,2,3] 
listB = listA
listB[0] = 100
# 이런 코드를 짠다면 
print(listA)
#를 했을 때
# A = [100,2,3] 이 출력된다.
# 리스트 복사가 일어난 것이 아니라 참조를 하게 되기 때문이다.
# 따라서 복사만 하고 싶을때는
lisB = listA[:]
# 와 같이 슬라이싱을 활용한 복사를 해야한다.
