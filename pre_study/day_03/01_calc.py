print("1 산술연산자 =====")
## ret : 숫자, 문자
## param : 숫자, 문자
a = 15 ; b = 7
print(a+b)
print(a-b)
print(a*b)
print(a/b)  ## 소숫점까지 연산
print(a%b)  ## 15 / 7 =  2...1
print(a//b) ## 정수까지 연산 (소숫점이하 삭제)
print(2**4) # 2의4승

a = "정우성" ; b = "정좌성"  ##문자, 문자 + 연산만 가능 : 문자열 결합
print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)  ## 소숫점까지 연산
#print(a%b)  ## 15 / 7 =  2...1
#print(a//b) ## 정수까지 연산 (소숫점이하 삭제)
#print(a**b) # 2의4승

a = "아기상어" ; b = 7
#print(a+b)
#print(a-b)
print(a*b)      ## 문자 * 숫자 : 문자반복
#print(a/b)  ## 소숫점까지 연산
#print(a%b)  ## 15 / 7 =  2...1
#print(a//b) ## 정수까지 연산 (소숫점이하 삭제)
#print(a**b) # 2의4승

print(2+3*4)
print((2+3)*4)

print("2 비교연산자 =====")
## ret : True,False (Bool)
## param : 숫자, 문자
'''
        수학표기    프로그램(부등호를 먼저표기)
초과    >            >
이상    ≧           >=  ,  =>에러
이하    ≦           <=
미만    <            <
같다    =            ==     = : 대입연산자
다르다  ≠            !=
'''
a = 30; b = 20
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)
##print(a => b)
#print(a = b)
print("------------------")
# ㄱ -> ㅎ
a = "정우성"; b = "정북성"
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)
print("------------------")
# 다른 자료형 크기 비교 불가
a = 12345; b = "정북성"
#print(a > b)
#print(a >= b)
#print(a <= b)
#print(a < b)
print(a == b)
print(a != b)


print("------------------")
## Bool 숫자로 치환 가능
## True -> 1,  False -> 0
a = True; b = False
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)
print("------------------")
## True -> 1,  False -> 0
a = -1; b = False
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)
print(a == b)
print(a != b)
print("------------------")
print( 5 + 3 > 10 - 1)

print("3 논리 연산자 =====")
#param :: True, False
#return :: True, False
'''
AND (&& 불가)   a and b 
OR   (|| 불가)  a or b 
부정 (! 불가)    not a

and
a   b   res
T   T   T
T   F   F
F   T   F
F   F   F

or
a   b   res
T   T   T
T   F   T
F   T   T
F   F   F

not
a   res
T   F
F   T

'''
a = False ; b = False
print(a and b)
print(a or b)
print(not a)
# print(a && b)
# print(a || b)
# print(!a)

age = 53
color = "하늘"

# ageChk = age <=25
# colorChk = color == "빨강"
# print("and" , ageChk and colorChk)
# print("or" , ageChk or colorChk)

print("and" , age <=25 and color == "빨강")
print("or" , age <=25+30 or color == "빨강")

print("4 대입 연산자 =====")
a = 5
print(a)
a = a+2
print(a)
a += 3
print(a)
a -= 2
print(a)
a *= 4
print(a)
a //= 5
print(a)
a **= 2
print(a)
a %= 7
print(a)

print("5 3항 연산자 =====")
a = False
## 조건 : Bool
print("참이지롱" if a else "거짓부렁")
    # True일때값   조건     False일때값

jum = 68
rr = "합격" if jum >= 80 else "불합격"
print(jum, rr)

rr =    "우수" if jum >= 80 else \
        "양호" if jum >= 60 else \
        "정상" if jum >= 40 else \
        "미달"
print(jum, rr)

'''
연산자우선순위
()
* / % // **
+ -
< <= >= > == !=
and or not

02_exam.py 를 생성하고
이름 , 국어, 영어, 수학 을 입력하고
총점, 평균을 계산하여 출력하세요

등급 
수  90 이상
우  80 이상
미  70 이상
양  60 이상
가  60 미만
'''