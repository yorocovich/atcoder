cards = list(map(int,input().split()))

num1 = cards[0]
cnt1 = 1
num2 = 0
cnt2 = 0

for i in range(1, 5):
  if cards[i] == num1:
    cnt1 += 1
    if cnt1 > 3:
      print("No")
      exit()
  elif cards[i] == num2:
    cnt2 += 1
    if cnt2 > 3:
      print("No")
      exit()
  else:
    if cards[i] != num1 and num2 == 0:
      num2 = cards[i]
      cnt2 = 1
    else:
      print("No")
      exit()
print("Yes")
