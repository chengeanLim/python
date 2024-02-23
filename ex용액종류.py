pH = int(input("수소 이온 지수를 입력하시오:"))

if pH >= 0 and pH <= 4 :
    print("pH : " %pH)
    print("강산성")

elif pH >= 5 and pH <= 6 :
    print("pH : ", pH)
    print("약산성")

elif pH==7 :
    print("pH : ", pH)
    print("중성")

elif pH >= 8 and pH <= 9 :
    print("pH : ", pH)
    print("약염기성")

elif pH >= 10 and pH <= 14 :
    print("pH : ", pH)
    print("강염기성")

else :
    print("값을 잘 못 입력 하였습니다.")
