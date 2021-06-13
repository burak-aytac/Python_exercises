left = set("qwertasdfgzxcvb")
right = set("yuiophjklmn")
word_clarusway = set("clarusway")
word_tester = set("tester")
word_polly = set("polly")
leftcheck = bool(left.intersection(word_clarusway))
rightcheck = bool(right.intersection(word_clarusway))
if leftcheck and rightcheck:
  print("Clarusway is comfortable word")
else :
  print("Clarusway is uncomfortable word")
leftcheck = bool(left.intersection(word_tester))
rightcheck = bool(right.intersection(word_tester))
if leftcheck and rightcheck:
  print("tester is comfortable word")
else:
    print("Tester is uncomfortable word")
leftcheck = bool(left.intersection(word_polly))
rightcheck = bool(right.intersection(word_polly))
if leftcheck and rightcheck:
  print("Polly is comfortable word")
else:
    print("Polly is uncomfortable word")