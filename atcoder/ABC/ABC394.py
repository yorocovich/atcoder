# A
s = input()
ans = ""
for i in range(len(s)):
  if s[i] == "2":
    ans += s[i]
  
print(ans)

# B
n = int(input())
text = []
for i in range(n):
  x = input()
  text.append((len(x),x))

text.sort()
print("".join(word for _, word in text))