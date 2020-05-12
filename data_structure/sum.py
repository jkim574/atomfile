import time


def sumofn(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sumofN2(n):
    start = time.time()

    thesum = 0
    for i in range(1, n+1):
        thesum += i

    end = time.time()

    answer = print(f"Sum is {thesum} required {end-start} seconds")
    return  answer


sumofN2(10)


print(sumofn(10))
