mount_500 = int(input())
mount_100 = int(input())
mount_50 = int(input())
sum = int(input())
res = 0

for x in range(0, mount_500 + 1):
  if x * 500 > sum:
    break
  else:
    for y in range(0, mount_100 + 1):
      if x * 500 + y * 100 > sum:
        break
      else:
        for z in range(0, mount_50 + 1):
          if x * 500 + y * 100 + z * 50 > sum:
            break
          elif x * 500 + y * 100 + z * 50 == sum:
            res += 1

# output
print(res)