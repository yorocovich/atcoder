def convert_to_vertical(lines):
    # 最長の行の長さを取得
    max_length = max(len(line) for line in lines)
    
    # 各行を最長の行の長さに合わせて'_'で埋める
    padded_lines = [line.ljust(max_length, '_') for line in lines]
    
    # 縦書きに変換し、各列を処理する
    vertical_lines = []
    for col in zip(*padded_lines):
        # 列を文字列に変換し、'_'以外の文字を抽出
        vertical_line = ''.join(char for char in reversed(col) if char != '_')
        if vertical_line:  # 空行を無視
            vertical_lines.append(vertical_line)
    
    return vertical_lines

# 入力を読み込む
N = int(input())
input_lines = []
for _ in range(N):
    s = input()
    if input_lines:
        # 既存の行よりも短い場合、'*'で埋める
        s += '*' * (max(len(line) for line in input_lines) - len(s))
    input_lines.append(s)

# 変換を実行
output_lines = convert_to_vertical(input_lines)

# 結果を出力
for line in output_lines:
    print(line)