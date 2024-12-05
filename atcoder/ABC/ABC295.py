n = int(input())
words = list(input().split())

for word in words:
  if word in ("and", "not", "that", "the", "you"):
    print("Yes")
    exit()

print("No")