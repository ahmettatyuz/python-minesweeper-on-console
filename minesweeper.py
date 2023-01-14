#20010011004 Ahmet Tatyuz

import random
import sys
while True:
    while True:
        mod = int(input("1-Gizli Mod\n2-Açık Mod\nSeçim: "))
        if mod !=1 and mod !=2:
            print("Hatalı Seçim !")
            continue
        break

    while True:
        boyut=int(input("Tarla Boyutu Ne Kadar Olsun (AxA) A: "))
        if boyut <10:
            print("Alanın boyutu en az 10x10 olmalıdır ! Tekrar Boyut Giriniz...")
        else:
            break


    kutular=[["?  " for x in range(boyut)] for y in range(boyut)]  #kutular oyun ekranını kastediyor.
    gizlikutular=[["?  " for x in range(boyut)] for y in range(boyut)]
    eklenecek_mayin_sayisi = (boyut ** 2) * 3 // 10 # Oyun alanının %30 u kadar mayın sayısı olacak.
    eklenen_mayin = 0
    while eklenen_mayin != eklenecek_mayin_sayisi:
        mayinx = random.randint(0, boyut - 1)
        mayiny = random.randint(0, boyut - 1)           #mayının çakışma durumu while dongüsü ile ayarlandı.
        if kutular[mayinx][mayiny] == "X  ":            #eklenen mayın eklenecek mayın sayısına eşit olana kadar
            continue                                    #dongu devam edecek.
        kutular[mayinx][mayiny] = "X  "
        eklenen_mayin += 1

    puan = 0

    dongu=True
    while dongu:

        # açık modu ekrana bastırma algoritması
        if mod == 2:
            print("   ", end="")
            for a in range(1, boyut + 1):               #burdaki kodların amacı oyun alanının üstünde ve
                if len(str(a)) == 2:                    #solunda sayıların çıkmasını sağlamak
                    print(f"{a} ", end="")              #maalesef biraz karmaşık oldu
                elif len(str(a)) == 3:
                    print(f"{a}", end="")
                elif a < 10:
                    print(f"{a}  ", end="")
            print()
            b = 1
            for i in kutular:
                if len(str(b)) == 2:
                    print(f"{b} ", end="")
                elif len(str(b)) == 3:
                    print(f"{b}", end="")
                elif b < 10:
                    print(f"{b}  ", end="")
                for j in i:
                    print(j, end="")
                b += 1
                print()

        print()
        # gizli modu ekrana bastırma algoritması
        if mod == 1:
            print("   ",end="")
            for a in range(1, boyut + 1):               #burdaki kodların amacı oyun alanının üstünde ve
                if len(str(a)) == 2:                    #solunda sayıların çıkmasını sağlamak
                    print(f"{a} ", end="")              #maalesef biraz karmaşık oldu
                elif len(str(a))==3:
                    print(f"{a}", end="")
                elif a<10:
                    print(f"{a}  ",end="")
            print()
            b=1
            for i in gizlikutular:
                if len(str(b))==2:
                    print(f"{b} ", end="")
                elif len(str(b))==3:
                    print(f"{b}", end="")
                elif b<10:
                    print(f"{b}  ",end="")
                for j in i:
                    print(j,end="")
                b+=1
                print()

        print(f"\nPuanınız :{puan}")

        ac_satir, ac_sutun=input("Açmak İstediğiniz Soru İşaretinin Koordinatını Arada Boşluk Bırakarak Giriniz(X.SATIR Y.SUTUN): ").split()
        print()
        ac_satir = int(ac_satir)
        ac_sutun = int(ac_sutun)
        if (ac_satir or ac_sutun)>boyut:
            print("Sınırların Dışına Çıkılamaz !")
            continue

        # Kullanıcının girdiği satır ve sütun numaralarını index olarak kullanmak içinn bir azaltıyorum
        ac_satir-=1
        ac_sutun-=1

        #     Mayına basma algoritması
        if kutular[ac_satir][ac_sutun]== "X  ":
            print("Mayına Bastınız ! Maalesef Kaybettiniz...")
            print(f"Puanınız {puan}")
            for i in kutular:
                for j in i:
                    print(j,end="")
                print()
            puan=0
            oyuntekrari=input("Oyunu tekrar oynamak için 1'e basınız!\nOyundan çıkmak için başka bir tuşa basınız!\nSeçim:")
            if oyuntekrari=="1":
                dongu=False
            else:
                print("Oyun Kapatılıyor...")
                sys.exit()


        #     Köşelerin Kontrol Algoritması
        elif (ac_satir == 0 and ac_sutun == 0) and kutular[ac_satir][ac_sutun]== "?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun + 1]== "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir + 1][ac_sutun]== "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir + 1][ac_sutun + 1]== "X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]= f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif (ac_satir == 9 and ac_sutun == 9) and kutular[ac_satir][ac_sutun]== "?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun - 1]== "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir - 1][ac_sutun]== "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir - 1][ac_sutun - 1]== "X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]= f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif (ac_satir == 0 and ac_sutun == 9) and kutular[ac_satir][ac_sutun]== "?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun - 1] == "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir + 1][ac_sutun] == "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir + 1][ac_sutun - 1] == "X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]= f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif (ac_satir == 9 and ac_sutun == 0) and kutular[ac_satir][ac_sutun]== "?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun + 1] == "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir - 1][ac_sutun] == "X  ":
                mayin_sayisi+=1
            if kutular[ac_satir - 1][ac_sutun + 1] == "X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]= f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        #     Kenarların Kontrol Algoritması
        elif ac_satir==0 and (ac_sutun!=0 or ac_sutun!=9) and kutular[ac_satir][ac_sutun]=="?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]=f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif ac_satir==9 and (ac_sutun!=0 or ac_sutun!=9) and kutular[ac_satir][ac_sutun]=="?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]=f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif ac_sutun==9 and (ac_satir!=0 or ac_satir!=9) and kutular[ac_satir][ac_sutun]=="?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun-1]=="X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]=f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        elif ac_sutun==0 and (ac_satir!=0 or ac_satir!=9) and kutular[ac_satir][ac_sutun]=="?  ":
            mayin_sayisi=0
            if kutular[ac_satir][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir-1][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun]=="X  ":
                mayin_sayisi+=1
            if kutular[ac_satir+1][ac_sutun+1]=="X  ":
                mayin_sayisi+=1
            kutular[ac_satir][ac_sutun]=f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        #     Aynı kutuyu tekrar seçemezsiniz!
        elif kutular[ac_satir][ac_sutun] !=("?  " or "X  "):
            print("Aynı Kutuyu Tekrar Seçemezsiniz !")
            puan -= 1   # Burda puanı 1 azaltmamın sebebi : Eğer oyuncu mayını seçmedikce puanı 1 artacaktır.
                        # Dolayısıyla ayın kutuyu seçtiğinde de puanı artacak. O yüzden aynı kutuyu seçtiği zaman
                        # puanı 1 azalacak bu elif bloğundan çıktıktan sonra 1 artacak.Yani puanı değişmiyor.

        #     Kenar veya Köşe Durumunda Olmayan Kutuların Kontrol Algoritması
        elif kutular[ac_satir][ac_sutun]== "?  ":
            mayin_sayisi=0
            for i in range(0,3):
                if kutular[ac_satir - 1][ac_sutun - 1 + i]== "X  ":
                    mayin_sayisi+=1
                if kutular[ac_satir][ac_sutun - 1 + i]== "X  ":
                    mayin_sayisi += 1
                if kutular[ac_satir + 1][ac_sutun - 1 + i]== "X  ":
                    mayin_sayisi += 1
            kutular[ac_satir][ac_sutun]= f"{mayin_sayisi}  "
            gizlikutular[ac_satir][ac_sutun] = f"{mayin_sayisi}  "

        puan += 1

        #     Kazanma Algoritması
        if puan == (boyut**2)*7//10:
            print("Tebrikler ! Oyunu Kazandınız ! Puanının: ",puan)
            oyuntekrari=input("Oyunu tekrar oynamak için 1'e basınız!\nOyundan çıkmak için başka bir tuşa basınız!\nSeçim:")
            if oyuntekrari=="1":
                dongu=False
            else:
                print("Oyun Kapatılıyor...")
                sys.exit()

