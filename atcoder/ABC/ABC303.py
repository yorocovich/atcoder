n = int(input())
s = input()
t = input()

s = s.replace("1","l")
s = s.replace("0","o")

t = t.replace("1","l")
t = t.replace("0","o")

print("Yes" if s == t else "No")