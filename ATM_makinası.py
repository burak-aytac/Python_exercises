from typing import runtime_checkable


print("""
      **************************
      Atm Makinasına Hoş Geldiniz
      İşlemler;
      1. Bakiye sorgulama
      2. Para Yatırma
      3. Para Çekme
      
      Programdan çıkmak için q'ya basınız
      ***************************
      """)
Bakiye = 1000

while True:
    try:
        islem = int(input("Yapmak istediğiniz işlemin numarasını yazınız : "))
        print(islem)
        if islem == 1:
            print("Bakiyeniz : %s $" % Bakiye)
            islem = input("Yapmak istediğiniz işlemin numarasını yazınız, çıkmak için q'ya basınız : ")
            print(islem)
            if islem == "2" :
                yeni_para = int(input("Yatırmak istediğiniz miktarı yazınız : "))
                print(yeni_para)
                Bakiye = Bakiye + yeni_para
                print("Yeni bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "3" :
                yeni_para = int(input("Çekmek istediğiniz miktarı yazınız : "))
                print(yeni_para)
                Bakiye = Bakiye - yeni_para
                print("Yeni bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "q":
                print("Teşekkür ederiz. İyi günler.")
                break
            else:
                print("Yanlış bir giriş yaptınız tekrar deneyin")
        elif islem == 2 :
            yeni_para = int(input("Yatırmak istediğiniz miktarı yazınız : "))
            print(yeni_para)
            Bakiye = Bakiye + yeni_para
            print("Yeni bakiyeniz : %s $" % Bakiye)
            islem = input("Yapmak istediğiniz işlemin numarasını yazınız, çıkmak için q'ya basınız : ")
            print(islem)
            if islem == "1" :
                print("Bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "3" :
                yeni_para = int(input("Çekmek istediğiniz miktarı yazınız : "))
                print(yeni_para)
                Bakiye = Bakiye - yeni_para
                print("Yeni bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "q":
                print("Teşekkür ederiz. İyi günler.")
                break
            else:
                print("Yanlış bir giriş yaptınız tekrar deneyin")   
        elif islem == 3 :
            yeni_para = int(input("Çekmek istediğiniz miktarı yazınız : "))
            print(yeni_para)
            Bakiye = Bakiye - yeni_para
            print("Yeni bakiyeniz : %s $" % Bakiye)
            islem = input("Yapmak istediğiniz işlemin numarasını yazınız, çıkmak için q'ya basınız : ")
            print(islem)
            if islem == "1" :
                print("Bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "2" :
                yeni_para = int(input("Yatırmak istediğiniz miktarı yazınız : "))
                print(yeni_para)
                Bakiye = Bakiye + yeni_para
                print("Yeni bakiyeniz : %s $" % Bakiye)
                break
            elif islem == "q":
                print("Teşekkür ederiz. İyi günler.")
                break
            else:
                print("Yanlış bir giriş yaptınız tekrar deneyin")
    except ValueError:
        print("Hatalı giriş yaptınız. İyi günler")
        break