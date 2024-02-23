#돈 투입 확인
int mainmenu()
{
    while(munu)
    {
        print("음류수 자판기"\n)
        print("돈을 400원 이상 투입 해주세요."\n)
        money=int(intput("투입액 :")
                  
        if (money < 400)
        {
            print("투입금이  모자릅니다. 돈을 다시 투입해주세요.")
            continue
        }

        else
        {
            print("%d원 투입되었습니다.\n", money)
            return 0
        }
                  
    }
}

#메뉴판 보여주기, 메뉴선택
int chart()
{
    Dcole=int("1000")
    Dcider=int("800")
    Dwater=int("400")
    while (Mainmenu)
    {
        print("다음 음류수증 해당 음류 번호를  선택해주세요\n")
        print("1. 콜라(1000원)\n")
        print("2. 사이다(800원)\n")
        print("3. 물(400원)\n")
        print("4. 자판기 종료\n")
        

        #메뉴 선택 제한걸기
        while(choose)
        {
            choose=int(input("메뉴를 선택해주세요. :"))
            if ((choose < 0) || (choose >4))
            {
                print("메뉴 선택을 잘 못 하셨습니다. 다시 선택 해주세요.\n")
                continue
            }

            else
            {
                print("%d번을 선택하였습니다.\n", choose)
                break
            }
        }

        #음류 수량 제한걸기
        while (number)
        {
            number=int(intput("원하는 음류수 수량을 입력해주세요. :"))
            print("\n")
            if((number < 0) || (number > 10))
            {
                print("수량을 잘못 입력하였습니다 다시 입력해주세요\n")
                continue
            }

            else
            {
                print("%개입니다.", number)
                break
            }
        }

        if (choose==1)
        {
            if(cola == 0)
            {
                print("콜라 재고가 부족합니다.\n 잔돈 %원을 환불하겠습니다.", money)
                break
            }

            elif((Dcola*number) > money)
            {
                print("돈이 부족합니다. 잔돈 %d원을 환불합니다." money)
                break
            }

            else
            {
                leftmoney = Dcola*number
                C_money = money - leftmoney
                cola -= number
                print("맛있게 드십시오.\n")
                print("잔돈 %d원 남았습니다.\n", leftmoney)
                print("남은 콜라 재고는 %d 입니다.\n", cola)   
            }

        elif(choose==2)
        {
            if(cider == 0)
            {
                print("사이다 재고가 부족합니다.\n 잔돈 %원을 환불하겠습니다.", money)
                break
            }

            elif((Dcider*number) > money)
            {
                print("돈이 부족합니다. 잔돈 %d원을 환불합니다." money)
                break
            }

            else
            {
                leftmoney = Dcider*number
                C_money = money - leftmoney
                cider -= number
                print("맛있게 드십시오.\n")
                print("잔돈 %d원 남았습니다.\n", leftmoney)
                print("남은 사이다 재고는 %d 입니다.\n", cider)
            }
        }

        elif(choose==3)
        {
            if(water == 0)
            {
                print("물 재고가 부족합니다.\n 잔돈 %원을 환불하겠습니다.", money)
                break
            }

            elif((Dwater*number) > money)
            {
                print("돈이 부족합니다. 잔돈 %d원을 환불합니다." money)
                break
            }

            else
            {
                leftmoney = Dwater*number
                C_money = money - leftmoney
                water -= number
                print("맛있게 드십시오.\n")
                print("잔돈 %d원 남았습니다.\n", leftmoney)
                print("남은 물 재고는 %d 입니다.\n", water)
            }
        }

        else
        {
            Y/N= int("자판기를 종류하시려면 1, 계속 이용하시려면 0을 입력하세요:")
            print("\n")
            
            if(Y/N == 0)
            {
                print("메뉴판을 다시 보여드립니다. 남은 돈은 %d 입니다.\n", money)
                return (mune)
            }
            
            elif(Y/N == 1)
            {
                print("자판기를 종류하겠습니다. 이용해주셔서 감사합니다. 잔돈은 %d 입니다.\n", money)
                break
            }

            else
            {
                printf("잘못 입렸했습니다. 다시 입력해주세요")
                continue
            }
        }
    }
    return 0
}




# number=음류 수량, money=투입금, C_money= 잔돈, choose=선택메뉴 leftmoney=남은돈
