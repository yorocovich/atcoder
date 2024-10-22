q = int(input())
char_count = {}
var = 0

for _ in range(q):
  input_value = list(map(int,input().split()))
  if input_value[0] == 3:
    print(len(char_count))
  elif input_value[0] == 1:
    if input_value[1] in char_count:
      char_count[input_value[1]] += 1
    else:
      char_count[input_value[1]] = 1
  elif input_value[0] == 2:
    char_count[input_value[1]] -= 1
    if char_count[input_value[1]] == 0:
        del char_count[input_value[1]]
