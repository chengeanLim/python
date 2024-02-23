def get_divisors(num):
    divisors = set()
    for i in range(2,num):
        if num % i == 0:
            divisors.add(i)
    return divisors

x = 48
y = 60
print(x, '의 진약수 :', get_divisors(x))
print(y, '의 진약수 :', get_divisors(y))
