s = input()
words = ['eraser','erase','dreamer','dream']

for t in words:
  while t in s:
    s = s.replace(t, '')

print("YES" if len(s) == 0 else "NO")