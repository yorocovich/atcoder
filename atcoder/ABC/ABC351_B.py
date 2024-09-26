n = int(input())

nums_a = nums_b = []
its_over = False

for _ in range(n):
  nums_a.append(input())

for i in range(n):
  chk_str = input()
  if nums_a[i] != chk_str:
    for j in range(n):
      if nums_a[i][j] != chk_str[j]:
        print(i+1,j+1)
        its_over = True
        break
  if its_over:
    break
