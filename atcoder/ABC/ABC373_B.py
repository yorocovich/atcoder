def sum_movement(string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    position = {char: index for index, char in enumerate(string)}
    
    total_distance = 0
    current_pos = position['A'] 
    
    for char in alphabet:
        next_pos = position[char]
        distance = abs(next_pos - current_pos)
        total_distance += distance
        current_pos = next_pos
    
    return total_distance

s = input()
ans = sum_movement(s)

print(ans)