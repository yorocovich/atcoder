s = input()
length = len(s)
max_num = (1 << length) - 1 
ans = max_num - int(s, 2)
print(format(ans, '0' + str(length) + 'b'))