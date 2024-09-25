n = int(input())

coders_name = []
coders_rate = []
for _ in range(n):
  s ,c = input().split()
  coders_name.append(s)
  coders_rate.append(int(c))

coders_name.sort()
print(coders_name[sum(coders_rate) % n])  
