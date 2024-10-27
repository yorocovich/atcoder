# A
s = input()

for i in range(16):
  if i % 2 == 1 and s[i] == "1":
    print("No")
    exit()

print("Yes")

# B
N = int(input())
results = []
for _ in range(N):
    results.append(input())

wins = []
for i in range(N):
    win_count = results[i].count('o')
    wins.append((win_count, -i, i+1))

wins.sort(reverse=True)
print(*[player for _, _, player in wins])