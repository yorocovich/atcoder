import bisect

class WallManager:
    def __init__(self, H, W):
        self.H = H
        self.W = W
        self.rows = [list(range(W)) for _ in range(H)]
        self.cols = [list(range(H)) for _ in range(W)]
        self.wall_count = H * W

    def remove_wall(self, r, c):
        if r in self.cols[c] and c in self.rows[r]:
            self.cols[c].remove(r)
            self.rows[r].remove(c)
            self.wall_count -= 1

    def find_nearest_wall(self, lst, val, lower=True):
        idx = bisect.bisect_left(lst, val)
        if lower:
            return lst[idx-1] if idx > 0 else None
        else:
            return lst[idx] if idx < len(lst) else None

    def place_bomb(self, R, C):
        R -= 1
        C -= 1
        if C in self.rows[R]:
            self.remove_wall(R, C)
        else:
            # 上方向
            upper = self.find_nearest_wall(self.cols[C], R, lower=True)
            if upper is not None:
                self.remove_wall(upper, C)
            # 下方向
            lower = self.find_nearest_wall(self.cols[C], R, lower=False)
            if lower is not None:
                self.remove_wall(lower, C)
            # 左方向
            left = self.find_nearest_wall(self.rows[R], C, lower=True)
            if left is not None:
                self.remove_wall(R, left)
            # 右方向
            right = self.find_nearest_wall(self.rows[R], C, lower=False)
            if right is not None:
                self.remove_wall(R, right)

def process_queries():
    H, W, Q = map(int, input().split())
    wall_manager = WallManager(H, W)
    
    for _ in range(Q):
        R, C = map(int, input().split())
        wall_manager.place_bomb(R, C)
    
    return wall_manager.wall_count

# メイン処理
print(process_queries())
