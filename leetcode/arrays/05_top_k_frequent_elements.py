# relatively tough question if solving with quickselect
# quickselect is used to find kth smallest, kth largest
# quickselect has two parts, partiton and select based on pivot
from collections import Counter
import random


def top_k_frequent(nums, k):

    # count the frequency of each number
    count = Counter(nums)
    # unique numbers
    unique = list(count.keys())

    def partiton(left, right, pivot_index):
        # get the pivot frequncy of pivot_index
        pivot_frequency = count[unique[pivot_index]]

        # move pivot to the end
        unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
        store_index = left

        # move less frequent element to the left
        for i in range(left, right):
            if count[unique[i]] < pivot_frequency:
                unique[store_index], unique[i] = unique[i], unique[store_index]
                store_index += 1

        # move to final position
        unique[store_index], unique[right] = unique[right], unique[store_index]
        return store_index

    def quickselect(left, right, k_smallest):
        # if only one element exists
        if left == right:
            return
        # pick random pivot index
        pivot_index = random.randint(left, right)
        # pivot in sorted postion
        pivot_index = partiton(left, right, k_smallest)

        if k_smallest == pivot_index:
            return
        # go left
        elif k_smallest < pivot_index:
            quickselect(left, pivot_index - 1, k_smallest)
        # go right
        else:
            quickselect(pivot_index, right, k_smallest)

    n = len(unique)

    quickselect(0, n - 1, k - 1)
    return unique[n - k:]


def top_k_frequent_sorting(nums, k):
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    arr = []
    for num, cnt in count.items():
        arr.append([cnt, num])
    arr.sort()

    result = []
    while len(result) < k:
        result.append(arr.pop()[1])
    return result


def top_k_frequent_bucket(nums, k):
    count = {}
    freq = []

    for i in range(len(nums) + 1):
        freq.append([])

    for num in nums:
        count[num] = 1 + count.get(num, 0)

    for num, cnt in count.items():
        freq[cnt].append(num)

    result = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            result.append(num)
            if len(result) == k:
                return result


nums = [1, 1, 1, 2, 2, 3]
k = 2

print(top_k_frequent(nums, k))
print(top_k_frequent_sorting(nums, k))
print(top_k_frequent_bucket(nums, k))
