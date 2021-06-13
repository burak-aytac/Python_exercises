def ebob(x,y) :
    list_x = []
    list_y = []
    set_ebob = {}
    for i in range(1,x+1) :
        if x % i == 0 :
            list_x.append(i)
    for i in range(1,y+1) :
        if y % i == 0:
            list_y.append(i)
    set_ebob = set(list_x).intersection(set(list_y))
    return set_ebob   
while True:
    x = input("EBOB'unu merak ettiğiniz ilk sayıyı giriniz, çıkmak için q'ya basınız : ")
    if x == "q":
        print("Teşekkürler")
        break
    x = int(x)
    y = int(input("EBOB'unu merak ettiğiniz ikinci sayıyı giriniz : "))
    print("Girdiğiniz iki sayının EBOB'unu veren küme : {}".format(ebob(x,y)))
