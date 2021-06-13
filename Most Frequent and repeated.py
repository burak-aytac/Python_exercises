def most_frequency(Numbers):
    count=0
    num=Numbers[0]
    for i in Numbers:
        new = Numbers.count(i)
        if new > count:
            count=new
            num=i
    return num
            
Numbers = [1, 3, 7, 4, 3, 0, 6, 3]
a = most_frequency(Numbers)
b = Numbers.count(a)
print("the most frequent number is {} and it was {} times repeated".format(a,b)) 