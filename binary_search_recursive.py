# Find item in a list using binary search recursively
def _helper(arr, item, low, high):
    mid = int((low + high) / 2)
    if (arr[mid] == item):
        return mid
    else:
        if (arr[mid] > item):
            return _helper(arr, item, low, mid - 1)
        else:
            return _helper(arr, item, mid + 1, high)


def binary_search_recursion(arr, item):
    low = 0
    high = len(arr) - 1
    return _helper(arr, item, low, high)


arr = [-10, -5, 1, 2, 3, 4, 5]
item = 3
index = binary_search_recursion(arr, item)
print(index)

