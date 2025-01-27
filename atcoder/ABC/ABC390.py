nums = list(map(int,input().split()))
i = 1
correct = 0
incorrect = 0
for num in nums:
  if num == i:
    correct += 1
    incorrect = 0 if incorrect != 2 else 2
  else:
    incorrect += 1
  i += 1

print("Yes" if correct == 3 and incorrect == 2 else "No")