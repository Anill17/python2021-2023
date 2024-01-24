def trap(heights):
    l, r = 0, len(heights)-1
    sum = 0 

    if not heights:
        return 0
    left_max, right_max = heights[l], heights[r]


    while l<r:
        if left_max < right_max:
            l += 1 
            left_max = max(left_max, heights[l])
            res += left_max - heights[l]

        else:
            r -= 1
            right_max = max(right_max, heights[r])
            res += right_max - heights[r]

    return res