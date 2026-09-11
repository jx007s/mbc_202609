a = 10  #변수 선언 및 초기화

## 리스트 변수 선언과 리스트 생성 및 초기화
arr1 = [11,22,33]
#인덱스  0  1  2

#변수 호출
print("a : ",a)
## 리스트변수 호출
print("arr1 : ",arr1)
## 리스트 원소 호출 : 배열명[인덱스]
print("arr1[0] : ",arr1[0])
#print("arr1[3] : ",arr1[3]) 존재하지 않는 인덱스 호출,대입불가

# - : 역방향 인덱스 사용
print("arr1[-1] : ",arr1[-1])
print("arr1[-2] : ",arr1[-2])
print("arr1[-3] : ",arr1[-3])
# print("arr1[-4] : ",arr1[-4])

## 리스트 원소 대입
arr1[1] = 2345
#arr1[3] = 5678
arr1[-1] = 9012

print("arr1 : ",arr1)
## len(배열명) : 배열의 원소갯수
print("len : ", len(arr1))


print("arr1[0] : ",arr1[0])
print("arr1[1] : ",arr1[1])
print("arr1[2] : ",arr1[2])

# tot = 0
# tot += arr1[0]
# print("tot:", tot)
# tot += arr1[1]
# print("tot:", tot)
# tot += arr1[2]
# print("tot:", tot)

tot = 0
i = 0
while i < 3:
    tot +=  arr1[i]
    print(i, arr1[i], tot)
    i+=1
    
print("tot:", tot)

# 05_even.py
## 34,56,78,86,23,46,17,83,22,64,75
## 짝수들의 합을 구하세요