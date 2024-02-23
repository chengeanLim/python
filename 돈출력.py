m = int(input('금액을 입력하세요:'))

a50000 = m//50000
b = m-a50000*50000

a10000 = b//10000
b -= a10000*10000

a5000 = b//5000
b -= a5000*5000

a1000 = b//1000
b -= a1000*1000

a500 = b//500
b -= a500*500

a100 = b//100
b -= a100*100

a50 = b//50
b -= a50*50

a10 = b//10
b -= a10*10

a0 = b%10

print('50000원',format(a50000),'개')
print('10000원',format(a10000),'개')
print('5000원',format(a5000),'개')
print('1000원',format(a1000),'개')
print('500원',format(a500),'개')
print('100원',format(a100),'개')
print('50원',format(a50),'개')
print('10원',format(a10),'개')
print('남은 돈',format(a0), '원')
