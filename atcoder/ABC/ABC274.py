# A
A, B = map(int, input().split())

result = B / A

formatted_result = round(result, 3)

print(f"{formatted_result:.3f}")

# B
h, w = map(int,input().split())
ans = [0] * w
for i in range(h):
  x = input()
  for j in range(w):
    if x[j] == "#":
      ans[j] += 1

print(*ans)