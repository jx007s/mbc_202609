print("type 1 >>>")
dan = 2
while dan < 10 :
    print("[",dan,"단]")
    
    gob = 1
    while gob < 10:
        print(dan ,"x",gob,"=",dan*gob)
        gob += 1
    dan += 1
    
print("type 2 >>>")

dan = 2
while dan < 10 :
    print(" [",dan,"단]  ", end="\t")
    dan += 1

print("")
gob = 1
while gob < 10:
    dan = 2
    while dan < 10 :
        print(dan ,"x",gob,"=",dan*gob, end="\t")
        dan += 1
    print("")
    gob += 1