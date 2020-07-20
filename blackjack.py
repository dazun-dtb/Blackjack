import random
import math
end=1
chip=100
while end!=0:
    trump=[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
    d=[]
    p=[]
    n=48
    pb=0
    db=0
    r=random.randrange(0,52)
    d.append(trump[r])
    del trump[r]
    r=random.randrange(0,51)
    d.append(trump[r])
    del trump[r]
    r=random.randrange(0,50)
    p.append(trump[r])
    del trump[r]
    r=random.randrange(0,49)
    p.append(trump[r])
    del trump[r]
    while True:
        kake=int(input("いくら賭けますか？あなたの所持金額は"+str(chip)+"ニャンです\n"))
        if kake<=chip and kake>=1:
            break
        else:
            print("その金額で賭けることはできません")
    chip=chip-kake
    print("ディーラー："+str(d[0])+',？')
    print("あなた："+str(p[0])+','+str(p[1]))
    if 1 in p :
        print("あなたの合計値は"+str(sum(p))+"または"+str(sum(p)+10)+"です")
        if sum(p)+10==21:
            pb=1
            print("ブラックジャック！")
    else:
        print("あなたの合計値は"+str(p[0]+p[1])+"です")
    while True:
        if n==48:
            hiku=int(input("スタンド：0、ヒット：１、ダブルダウン：2、サレンダー：3\n"))
        else:
            hiku=int(input("スタンド：0、ヒット：１\n"))
        if hiku==3:
            print("あなたはサレンダーしました")
            chip=chip+kake-math.ceil(kake/2)
            print("増減：-"+str(math.ceil(kake/2)))
            break
        if hiku==1 or hiku==2:
            if hiku==2 and chip>=kake:
                chip=chip-kake
                kake=kake*2
                print("ダブルダウンが選ばれたので掛け金を倍にしました")
            elif hiku==2:
                print("所持金が足りません")
                continue
            r=random.randrange(0,n)
            p.append(trump[r])
            print("あなたは「"+str(trump[r])+"」を引きました")
            print("あなたの手札："+str(p))
            if 1 in p and sum(p)+10<=21:
                print("あなたの合計値は"+str(sum(p))+"または"+str(sum(p)+10)+"です")
            else:
                print("あなたの合計値は"+str(sum(p))+"です")
            del trump[r]
            n=n-1
            if sum(p)>21:
                print("バーストしました\nあなたの負けです")
                print("増減：-"+str(kake))
                break
            if hiku==2:
                break
        if hiku==0:
            break
    if sum(p)<=21 and hiku!=3:
        print("ディーラー："+str(d[0])+','+str(d[1]))
        if 1 in d and sum(d)+10==21:
            db=1
            print("ブラックジャック！")
        else:
            while sum(d)<17:
                if 1 in d:
                    if sum(d)+10>=17 and sum(d)+10<=21:
                        break
                r=random.randrange(0,n)
                d.append(trump[r])
                n=n-1
                print("ディーラーは「"+str(trump[r])+"」を引きました")
                del trump[r]
                print("ディーラーの手札："+str(d))
                if 1 in d and sum(d)+10<=21:
                    print("ディーラーの合計値は"+str(sum(d))+"または"+str(sum(d)+10)+"です")
                else:
                    print("ディーラーの合計値は"+str(sum(d))+"です")
                if sum(d)>21:
                    print("ディーラーがバーストしました\nあなたの勝ちです")
                    if pb==1:
                        print("ブラックジャックなので掛け金の半分を追加で獲得しました")
                        chip=chip+kake*2+math.floor(kake/2)
                        print("増減：+"+str(kake*2+math.floor(kake/2)))
                    else:
                        chip=chip+kake*2
                        print("増減：+"+str(kake*2))
                    break
    if sum(p)<=21 and sum(d)<=21 and hiku!=3:
        p_sum=0
        d_sum=0
        if 1 in p and sum(p)+10<=21:
            p_sum=sum(p)+10
        else:
            p_sum=sum(p)
        if pb==1:
            print("あなたの合計値は"+str(p_sum)+"(ブラックジャック)")
        else:
            print("あなたの合計値は"+str(p_sum))
        if 1 in d and sum(d)+10<=21:
            d_sum=sum(d)+10
        else:
            d_sum=sum(d)
        if db==1:
            print("ディーラーの合計値は"+str(d_sum)+"(ブラックジャック)")
        else:
            print("ディーラーの合計値は"+str(d_sum))
        if p_sum>d_sum or (pb==1 and db==0):
            print("よって、あなたの勝ちです")
            if pb==1:
                print("ブラックジャックなので掛け金の半分を追加で獲得しました")
                chip=chip+kake*2+math.floor(kake/2)
                print("増減：+"+str(kake*2+math.floor(kake/2)))
            else:
                chip=chip+kake*2
                print("増減：+"+str(kake*2))
        elif d_sum>p_sum or (pb==0 and db==1):
            print("よって、あなたの負けです")
            print("増減：-"+str(kake))
        else:
            print("引き分けです")
            chip=chip+kake
    if chip==0:
        print("所持金を失ったので所持金をリセットします")
        chip=100
    print("現在の所持金は"+str(chip)+"ニャンです")
    end=int(input("ゲームを続ける場合は１を、ゲームを終了するには０を入力してEnterキーを押してください\n"))
