# A
ranker_dict = {"tourist":3858
,"ksun48":3679
,"Benq":3658
,"Um_nik":3648
,"apiad":3638
,"Stonefeang":3630
,"ecnerwala":3613
,"mnbvmar":3555
,"newbiedmy":3516
,"semiexp":3481}

s = input()

print(ranker_dict[s])

# B
n = int(input())
ans = ""
for i in range(n+1):
  for j in range(1,10):
    if n % j == 0 and i % (n / j) == 0:
      ans += str(j)
      break
    if j == 9:
      ans += "-"

print(ans)