a = 0
sum = 0
while a<100:
    a += 1
    if a % 5 == 0:
        print(a)
        sum = sum + a
print("total is: ", sum)
