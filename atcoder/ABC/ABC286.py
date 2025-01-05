n, p, q, r, s = map(int,input().split())
nums = list(map(int,input().split()))
nums_before_p = []
nums_pq = []
nums_qr = []
nums_rs = []
nums_after_s = []
ans = []

for i in range(n):
  if i + 1 < p:
    nums_before_p.append(nums[i])
  elif p <= i + 1 <= q:
    nums_pq.append(nums[i])
  elif q < i + 1 < r:
    nums_qr.append(nums[i])
  elif r <= i + 1 <= s:
    nums_rs.append(nums[i])
  else:
    nums_after_s.append(nums[i])

ans = nums_before_p + nums_rs + nums_qr + nums_pq + nums_after_s

print(*ans)