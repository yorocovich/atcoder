h,w = map(int,input().split())
s_i,s_j = map(int,input().split())
cells = []
for i in range(h):
   cells.append(list(input())) 

move = input()

now_i = s_i - 1
now_j = s_j - 1
for i in range(len(move)):
  if move[i] == 'U':
    if now_i != 0 and cells[now_i-1][now_j] != '#':
      now_i -= 1
  elif move[i] == 'D':
    if now_i+1 != h and cells[now_i+1][now_j] != '#':
      now_i += 1
  elif move[i] == 'L':
    if now_j != 0 and cells[now_i][now_j-1] != '#':
      now_j -= 1
  elif move[i] == 'R':
    if now_j+1 != w and cells[now_i][now_j+1] != '#':
      now_j += 1

print(now_i+1,now_j+1)