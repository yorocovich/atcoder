# A
a, b, c = map(int,input().split())

if a == b == c:
  print("Yes")
else:
  if a == (b + c) or b == (a + c) or c == (a + b):
    print("Yes")
  else:
    print("No")

# B
H, W, x, y = map(int, input().split())

grid = []
for _ in range(H):
    line = input()
    grid.append(list(line))

order = input()

start_x, start_y = x-1, y-1

visited_houses = set()

def check_and_add_house(x: int, y: int):
    if 0 <= x < H and 0 <= y < W and grid[x][y] == '@':
        visited_houses.add((x, y))

current_x = start_x
current_y = start_y

check_and_add_house(current_x, current_y)

for char in order:
    next_x, next_y = current_x, current_y
    
    if char == 'L' and current_y > 0 and grid[current_x][current_y-1] != '#':
        next_y = current_y - 1
    elif char == 'R' and current_y < W-1 and grid[current_x][current_y+1] != '#':
        next_y = current_y + 1
    elif char == 'U' and current_x > 0 and grid[current_x-1][current_y] != '#':
        next_x = current_x - 1
    elif char == 'D' and current_x < H-1 and grid[current_x+1][current_y] != '#':
        next_x = current_x + 1
    
    check_and_add_house(next_x, next_y)
    
    current_x, current_y = next_x, next_y

print(f"{current_x + 1} {current_y + 1} {len(visited_houses)}")

# C
N = int(input())
H = list(map(int, input().split()))

def find_max_buildings():
   height_positions = {}
   for i, h in enumerate(H):
       if h not in height_positions:
           height_positions[h] = []
       height_positions[h].append(i)
   
   max_count = 1
   
   for positions in height_positions.values():
       pos_set = set(positions)
       L = len(positions)
       if L <= max_count:
           continue
           
       for i in range(L):
           start = positions[i]
           for j in range(i+1, min(i+L, L)):
               d = positions[j] - start
               if start + d * (max_count-1) >= N:
                   continue
               
               count = 1
               curr = start + d
               while curr < N and curr in pos_set:
                   count += 1
                   curr += d
               
               if count > max_count:
                   max_count = count

   return max_count

print(find_max_buildings())