#!/usr/bin/python3
def rain(walls):
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    total = 0

    while left < right:
        if walls[left] < walls[right]:
            left_max = max(left_max, walls[left])
            total += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            total += right_max - walls[right]
            right -= 1

    return total
walls = [0,1,0,2,0,3,0,4]
print(rain(walls))  # Output: 6

