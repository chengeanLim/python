sum = 0

limit=int(input("어디까지 계산 할까요:"))

 for i in range(1, limit+1) :
     sum += i

print("1부터", limit, "까지의 정수의 합 = ", sum)
