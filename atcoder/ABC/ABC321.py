# A
n = list(input())

for i in range(1,len(n)):
  if int(n[i-1]) <= int(n[i]):
    print("No")
    exit()

print("Yes")

# B
def calculate_required_score(N, X, scores):
    for final_score in range(101):
        all_scores = scores + [final_score]
        sorted_scores = sorted(all_scores)
        middle_scores = sorted_scores[1:-1]
        total = sum(middle_scores)
        if total >= X:
            return final_score            
    return -1

N, X = map(int, input().split())
scores = list(map(int, input().split()))
result = calculate_required_score(N, X, scores)
print(result)