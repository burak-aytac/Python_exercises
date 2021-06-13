#amstrong sayısı tüm basamakların teker teker hepsinin küp kendine eşit olan sayı
is_amstrong = input("Lütfen bir sayı giriniz : ")
digits = len(is_amstrong)
summ = 0
if not is_amstrong.isdigit():
    print(is_amstrong, "is invalid. Enter numeric value")
elif int(is_amstrong) >= 0:
    for i in range(digits):
        summ = summ + int(is_amstrong[i])**digits
    if summ == int(is_amstrong) :
        print(is_amstrong, "is an Amstrong number")
    else :
        print(is_amstrong, "isn't an Amstrong number")
else:
    print(is_amstrong, "isn't an Amstrong number")