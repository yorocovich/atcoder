def can_divide(members, max_group):
    def dfs(index, group1, group2):
        if index == len(members):
            return max(group1, group2) <= max_group
        
        if group1 + members[index] <= max_group:
            if dfs(index + 1, group1 + members[index], group2):
                return True
        
        if group2 + members[index] <= max_group:
            if dfs(index + 1, group1, group2 + members[index]):
                return True
        
        return False

    return dfs(0, 0, 0)

def find_min_max_sum(members):
    left = max(members)
    right = sum(members)
    
    while left < right:
        mid = (left + right) // 2
        if can_divide(members, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

N = int(input())
members = list(map(int, input().split()))

result = find_min_max_sum(members)
print(result)