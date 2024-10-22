def min_operations(N, Q, instructions):
    def update_movable(pos, other_pos):
        clockwise = []
        counter_clockwise = []
        current = (pos + 1) % N
        while current != other_pos:
            clockwise.append(current)
            current = (current + 1) % N
        current = (pos - 1) % N
        while current != other_pos:
            counter_clockwise.append(current)
            current = (current - 1) % N
        return clockwise, counter_clockwise

    L, R = 0, 1  # 0-indexed
    total_moves = 0
    
    for hand, target in instructions:
        target -= 1  # Convert to 0-indexed
        if hand == 'L':
            clockwise, counter_clockwise = update_movable(L, R)
            if target == R:
                return -1
            if target in clockwise:
                moves = clockwise.index(target) + 1
            elif target in counter_clockwise:
                moves = counter_clockwise.index(target) + 1
            else:
                moves = 0
            total_moves += moves
            L = target
        else:  # hand == 'R'
            clockwise, counter_clockwise = update_movable(R, L)
            if target == L:
                return -1
            if target in clockwise:
                moves = clockwise.index(target) + 1
            elif target in counter_clockwise:
                moves = counter_clockwise.index(target) + 1
            else:
                moves = 0
            total_moves += moves
            R = target

    return total_moves

N, Q = map(int, input().split())
instructions = [input().split() for _ in range(Q)]
instructions = [(h, int(t)) for h, t in instructions]

result = min_operations(N, Q, instructions)
print(result)