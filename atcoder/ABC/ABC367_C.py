def generate_sequences(n: int, k: int, r: list) -> list:
    def backtrack(index: int, current_sum: int, sequence: list):
        if index == n:
            if current_sum % k == 0:
                sequences.append(tuple(sequence))
            return
        
        for i in range(1, r[index] + 1):
            sequence[index] = i
            backtrack(index + 1, current_sum + i, sequence)

    sequences = []
    backtrack(0, 0, [0] * n)
    return sorted(sequences)

# 入力
n, k = map(int, input().split())
r = list(map(int, input().split()))

# 数列生成とソート
valid_sequences = generate_sequences(n, k, r)

# 出力
for seq in valid_sequences:
    print(*seq)