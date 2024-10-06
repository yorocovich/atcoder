hasNext = True
a = []
while hasNext:
  str = int(input())
  a.append(str)
  if str == 0:
    hasNext = False

while len(a) > 0:
  print(a.pop())