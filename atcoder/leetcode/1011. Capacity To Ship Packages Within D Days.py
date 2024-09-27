class Solution(object):
    def shipWithinDays(self, weights, days):
        # days以内でさばけるか
        def can_ship_within_days(capacity_a_day):
            spend_days = 1
            total_weight_a_day = 0
            for weight in weights:
                if total_weight_a_day + weight > capacity_a_day:
                    spend_days += 1
                    total_weight_a_day = weight
                else:
                    total_weight_a_day += weight

                if spend_days > days:
                    return False
            return True

        min_a_day = max(weights)
        max_a_day = sum(weights)

        # 二分探索
        while min_a_day < max_a_day:
            median = (min_a_day + max_a_day) // 2
            if can_ship_within_days(median):
                max_a_day = median
            else:
                min_a_day = median + 1
    
        return min_a_day
