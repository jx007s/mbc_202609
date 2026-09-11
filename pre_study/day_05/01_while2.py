# 1 -> 100 짝수들의 합

i = 1
tot = 0
while i<=100:
    if i%2==0:
        tot+=i
        print(i,tot)
    i+=1
print("풀이 1 :", tot)

i = 0
tot = 0
while i<=100:
    tot+=i
    print(i,tot)
    i+=2
    
print("풀이 2 :", tot)

i = 1
tot = 0

i+=i%2
while i<=100:
    tot+=i
    print(i,tot)
    i+=2
    
print("풀이 3 :", tot)