#forloop
for i in range(1,6):
    print("*" * i)
for i in range(1,10):
    print(i) 
for i in range(100):
    print("sorry !")   

#even odd
for i in range(20):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
for i in range(2,21,2):
    print(i,"is even")
    #break
    for i in range(1,51):
        if i==25:
            break
        if (i%3==0):
            print(i,"is divisible by 3")
#continue
for i in range(1,51):
    if i==25:
        continue
    if (i%3==0):
        print(i,"is divisible by 3")
      