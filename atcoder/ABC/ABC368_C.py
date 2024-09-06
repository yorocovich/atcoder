N = int(input())
E = list(map(int,input().split()))
T = 0
for i in range(len(E)):
  while E[i] > 0:
    if E[i] >= 5:
      T += E[i] // 5 * 3
      E[i] = E[i] % 5
    else:
      T += 1
      if T % 3 == 0:
        E[i] -= 3
      else:
        E[i] -= 1

print(T)