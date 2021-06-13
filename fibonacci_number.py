fibonacci = []
for i in range(0,56):
    i = i-1 + i-2
    if (i > 0) and (i <= 55):
        fibonacci.append(i)
print(fibonacci)