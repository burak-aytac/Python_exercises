my_name = "burak"
new_name = input("Lütfen isminizi giriniz : ")
password = "W@12"
if new_name.lower() == my_name:
    print("Hello, {}! The password is : {}".format(my_name.upper(),password))
else:
    print("Hello, {}! See you later.".format(new_name.upper()))