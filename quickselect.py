def quickselect(arr, k):

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]

        # move pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        # move smaller elements than pivot to the left of store index
        for i in range(left, right):
            if arr[i] < pivot_value:  # k_smallest hence <
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        # move to original place
        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index

    def select(left, right, k_smallest):

        # if it contains only one element
        if left == right:
            return arr[left]

        pivot_index = partition(left, right, k_smallest)
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)

    # since arr is 0 based and k is one based
    return select(0, len(arr) - 1, k - 1)


arr = [-1, 4, 0, 6, 2, 3]
k = 2
print(quickselect(arr, k))
