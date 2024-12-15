# A
n = int(input())
steps = list(map(int,input().split()))
ans = []
step = 0

for i in range(1,len(steps)+1):
  step += steps[i-1]
  if i % 7 == 0:
    ans.append(step)
    step = 0

print(*ans)

# B
def is_palindrome(text: str) -> bool:
  cleaned_text = "".join(text.lower().split())
  left = 0
  right = len(cleaned_text) - 1

  while left < right:
    if cleaned_text[left] != cleaned_text[right]:
      return False
    left += 1
    right -= 1
    
  return True

n = int(input())
strings = []
for i in range(n):
  strings.append(input())

for i in range(len(strings)):
  for j in range(len(strings)):
    if i == j:
      continue
    else:
      if is_palindrome(strings[i]+strings[j]):
        print("Yes")
        exit()

print("No")