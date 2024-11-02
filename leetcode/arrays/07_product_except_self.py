# calcualte prefix and postfix
# pass in the prefix result to postfix
# go reverse for postfix


def product_except_self(nums):

    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        # populate the result going in forward direction
        result[i] = prefix
        prefix *= nums[i]  # update prefix

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        # update existing result, move in reverse on original array
        result[i] *= postfix
        postfix *= nums[i]

    return result


nums = [1, 2, 3, 4]
print(product_except_self(nums))
