name = "장동건"
kor = 88
eng = 86
mat = 82
tot = kor + eng + mat
avg = tot / 3
print("이름 : ", name)
print("국어 : ", kor)
print("영어 : ", eng)
print("수학 : ", mat)
print("총점 : ", tot)
print("평균 : ", avg)
'''
85.33333333333333
*100
8533.333333333333
//1
8533
/100
85.33
'''
avg2 = avg*100//1/100
print("평균2 : ", avg2)

grade =     "수" if avg >= 90 else \
            "우" if avg >= 80 else \
            "미" if avg >= 70 else \
            "양" if avg >= 60 else \
            "가"

print("등급 : ", grade)

