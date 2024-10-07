strs = input()
ans = ""
start = strs.rfind(".")+1 if strs.rfind(".") != -1 else 0
print(strs[start:])