s = input()
t = input()

idt = ids = 0
correct_pos = []

while idt <= len(t):
  if s[ids] == t[idt]:
    correct_pos.append(idt+1)
    ids += 1
    idt += 1
    if ids == len(s):
      break
  else:
    idt += 1
print(*correct_pos)