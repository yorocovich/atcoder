# A
s = input()
s_list = list(s)

for i in range(0, len(s) - 1, 2):
    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

ans = "".join(s_list)
print(ans) 

# B
k = int(input())
calls = list(map(int, input().split()))
called = set()  # 高速な集合を使用
ans = []

# callsの番号がcalledに含まれていない場合、追加する
for i in range(k):
    if i + 1 not in called:  # ここを残します
        called.add(calls[i])

# 1からkまでのうち、called に含まれていないものを探す
for j in range(1, k + 1):
    if j not in called:
        ans.append(j)

# 結果を出力
print(len(ans))
print(*ans)
