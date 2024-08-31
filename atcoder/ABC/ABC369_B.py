n = int(input())

key_types = []
l_pos = r_pos = 0
l_first = r_first = True
diff = 0

for _ in range(n):
  pos,direction = input().split()

  if direction == 'L':
    if l_first == True:
      l_first = False
      l_pos = int(pos)
      continue
    diff += abs(l_pos - int(pos))
    l_pos = int(pos)

  else:
    if r_first == True:
      r_first = False
      r_pos = int(pos)
      continue
    diff += abs(r_pos - int(pos))
    r_pos = int(pos)
    
print(diff)