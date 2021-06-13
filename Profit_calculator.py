
def profit_calculator(sales):
  total = 0
  for i in sales:
    total = total + round(sales[i])
  return total
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
a = profit_calculator(sales)
print("the profit will be : {}".format(a))

#toplamın küsüratını silme
def trueprofit(sales):
  x = sales["cost_value"]
  y = sales["sell_value"]
  z = sales["inventory"]
  last_value = round((y-x)*z)
  return last_value
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
print(trueprofit(sales))

#küsürat silme
def newfund(sales):
  Listem = []
  for i in sales:
    i = round(sales.get(i),2)
    Listem.append(i)
  return Listem
sales = {
  "cost_value": 31.87,
  "sell_value": 45.00,
  "inventory": 1000
}  
print(newfund(sales))

#hatasını bulamadım
fiyatlar = {}
domates = float(input("Domates fiyatını girin : "))
biber = float(input("Biber fiyatını girin : "))
patlican = float(input("Patlıcan fiyatını girin : "))
my_dict = {}
def payroll(my_dict):
  fiyatlar = {"domates" : domates,
              "biber" : biber,
              "patlican" : patlican}
  for i in fiyatlar.keys:
    fiyatlar = round(fiyatlar[i])
    my_dict = fiyatlar
  return fiyatlar
print(payroll(my_dict))

#zip ile tuple birleştirme
z = ["domates", "biber", "patlıcan"]
t = []
for i in range(len(z)):
  t.append(int(input(f"{z[i]} fiyatını giriniz")))
x = zip(tuple(z),tuple(t))
print(dict(x))