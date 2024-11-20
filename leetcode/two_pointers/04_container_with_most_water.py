def max_water(heights):

    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        max_area = max(max_area, area)
        if heights[left] >= heights[right]:
            right -= 1
        else:
            left += 1

    return max_area


heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water(heights))
