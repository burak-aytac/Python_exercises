n = int(input("Bir sayı girin : "))
count = 0
for i in range(1, n+1):
    if not n % i :
        count += 1
if (n==0) or (n==1) or (count >= 3) :
    print(n, "is not prime number")
else:
    print(n, "is a prime number")