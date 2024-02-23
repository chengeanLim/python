import math

A = fltoat(input("A="))
B = fltoat(input("B="))
C = fltoat(input("C="))

D = B*B-4*A*C

if A == 0 :
    print("x=", -C/B)

if D == 0 :
    print("x=", -B/(2.0*A))
elif D > 0 :
    primt("x1= ", (-B +math.sqrt(D))/(2.0*A))
    primt("x2= ", (-B -math.sqrt(D))/(2.0*A))

else :
    print("실근이 존재하지 않음")
    
