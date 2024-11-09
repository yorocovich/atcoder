# A
n = input()

print(n[1]+n[2]+n[0],n[2]+n[0]+n[1])

# B
N, K = map(int, input().split())
S = input()

def count_consumable(n):
    count = 0
    while n >= K:
        n -= K
        count += 1
    return count

teeth = [len(s) for s in S.split('X') if s]
ans = sum(count_consumable(t) for t in teeth)
print(ans)

# D
def solve():
    # 初期化: 100本の種木(高さはすべて-1で初期化。-1は植物が植えられていないことを示す)
    trees = [-1] * 100
    results = []
    
    # クエリ数を読み込む
    Q = int(input())
    
    # 高さの補正値（クエリ2による累積の高さ増加）
    height_adjustment = 0
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        query_type = query[0]
        
        if query_type == 1:
            # 空いている種木を探して植物を植える
            for i in range(100):
                if trees[i] == -1:
                    # 植物を植える（現在の補正値を考慮して-height_adjustmentを設定）
                    trees[i] = -height_adjustment
                    break
        
        elif query_type == 2:
            T = query[1]
            # 高さの補正値を更新
            height_adjustment += T
        
        else:  # query_type == 3
            H = query[1]
            count = 0
            # 高さH以上の植物を数え、収穫する
            for i in range(100):
                if trees[i] != -1 and trees[i] + height_adjustment >= H:
                    count += 1
                    trees[i] = -1
            results.append(count)
    
    # 結果を出力
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()
