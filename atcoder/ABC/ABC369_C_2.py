def run_length_compression(B):
    # B が空リストの場合、空のリストを返す
    if not B:
      return []
    
    # ランレングス圧縮の結果を保持するリスト
    compressed = []
  
    # 最初の要素を設定
    current_value = B[0]
    count = 1
    
    # B の2番目の要素からループを開始
    for i in range(1, len(B)):
      if B[i] == current_value:
          # 連続して同じ値が現れた場合、カウントを増加
          count += 1
      else:
          # 違う値が現れた場合、ペア (値, カウント) を追加し、カウントをリセット
          compressed.append((current_value, count))
          current_value = B[i]
          count = 1
    
    # 最後の値のペアを追加
    compressed.append((current_value, count))
    
    return compressed

def sum_count(d):
    return d * (d + 1) // 2

N = int(input())
A = list(map(int, input().split()))
B = []

for i in range(N - 1):
  B.append(A[i + 1] - A[i])

ans = N # l=rの分

# ランレングス圧縮
compressed_B = run_length_compression(B)

for value, count in compressed_B:
    ans += sum_count(count)
    
print(ans)
