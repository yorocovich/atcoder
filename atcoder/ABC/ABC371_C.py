def binary_search(nums ,x):
  left , right = 0 , len(nums)
  while left < right:
    mid = (left + right) // 2
    if nums[mid][0] < x:
      left = mid + 1
    else:
      right = mid
  return left

N = int(input())
X = list(map(int,input().split()))
P = list(map(int,input().split()))
Q = int(input())
#クエリをまとめて配列にする
queries = [list(map(int, input().split())) for _ in range(Q)] 

#村の座標と人口をまとめて配列にする
villages = list(zip(X, P)) 

#累積和を計算
cumulative_sum = [0] * (N + 1)
for i in range(N):
  cumulative_sum[i + 1] = cumulative_sum[i] + villages[i][1]

#クエリを処理
for L, R in queries:
    left = binary_search(villages, L)
    right = binary_search(villages, R + 1)
    print(cumulative_sum[right] - cumulative_sum[left])
