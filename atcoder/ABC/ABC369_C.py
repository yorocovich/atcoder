# TLE

def count_tohsa(N, arr):
  cnt = 0
  for l in range(N):
    for r in range(l, N):
      if r - l + 1 < 3:
        cnt += 1
      else:
        is_tohsa = True
        diff = arr[l + 1] - arr[l]
        for i in range(l + 2, r + 1):
          if arr[i] - arr[i - 1] != diff:
            is_tohsa = False
            break # 等差じゃなくなったら以降ループやめ
        if is_tohsa:
          cnt += 1
  return cnt

N = int(input())
nums = list(map(int, input().split()))

ans = count_tohsa(N, nums)

print(ans)