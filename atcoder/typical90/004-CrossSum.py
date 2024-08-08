h, w = map(int, input().split())
list_h = []

for _ in range(h):
  list_w = [int(_) for _ in input().split()]
  # 横の列の合計
  list_w.append(sum(list_w))
  list_h.append(list_w)

#縦の列の合計
sums = [sum(col) for col in zip(*list_h)]
list_h.append(sums)

#出力
plist_j = []

for i in range(h):
  plist_i = []
  for j in range(w):
    plist_i.append(list_h[i][w] + list_h[h][j] - list_h[i][j])
  plist_j.append(plist_i)  

for row in plist_j:
  print(' '.join(map(str, row)))