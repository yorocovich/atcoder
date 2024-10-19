def solve_box_packing(N, A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    B.append(0)  # 番兵として0を追加

    new_box_size = 0
    j = 0

    for i in range(N):
        if A[i] > B[j]:
            if new_box_size > 0:
                return -1  # 2つ目の新しい箱が必要な場合
            new_box_size = A[i]
        else:
            j += 1

    return new_box_size

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = solve_box_packing(N, A, B)
print(result)