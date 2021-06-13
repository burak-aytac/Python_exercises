#3'lü dizinin çeşitli kombinasyonu
num = [1,2,3]
solution = [[]]
# solution-1 = [[1],[2],[3]]
# solution-2 = [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
# solution-3 = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
num_set = set(num)
for index in range(len(num)) :
   solution =  [i + [j] for i in solution for j in num_set.difference(set(i))]
   print(solution)
solution    