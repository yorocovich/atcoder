s = input()
s_list = list(s)

for i in range(0, len(s) - 1, 2):
    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

ans = "".join(s_list)
print(ans) 
