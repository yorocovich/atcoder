def is_valid(n, now_i: int, now_j: int, move_i: int, move_j: int) -> bool:
    next_i = now_i + move_i
    next_j = now_j + move_j
    
    if next_i < 0 or next_i >= n:
        return False
        
    if next_j < 0 or next_j >= n:
        return False
        
    return True

n, m = map(int,input().split())
knight = []
for _ in range(m):
    y, x = map(int,input().split())
    knight.append([y-1, x-1])

ng_pos = set()
for i, j in knight:
    ng_pos.add((i,j))
    #8方向のナイトの動き
    moves = [
        (-2,-1), (-1,-2), (1,-2), (2,-1),
        (-2,1), (-1,2), (1,2), (2,1)
    ]
    for di, dj in moves:
        if is_valid(n, i, j, di, dj):
            ng_pos.add((i+di, j+dj))

print(n * n - len(ng_pos))