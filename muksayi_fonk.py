def muk_sayi(sayi) :
    numbers = []
    toplam = 0
    sayi = int(sayi)
    for i in range(1,sayi) :
        if sayi % i == 0:
            numbers.append(i)
    print(numbers)
    sayi = int(sayi)
    for i in numbers :
        toplam += i 
    print(toplam)
    if sayi == toplam :
        return True
    else :
        return False
while True:
    sayi = input("Mükemmel sayıyı öğrenmek için bir sayı giriniz çıkmak için q'ya basınız : ")
    if sayi == "q":
        print("Teşekkürler. İyi günler.")
        break
    elif muk_sayi(sayi) == True :
        print("%s bir mükemmel sayıdır" %sayi)
        break
    else:
        print("%s bir mükemmel sayı değildir" %sayi)
        break
        