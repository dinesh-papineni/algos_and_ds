# Find item in a list using binary search
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if (arr[mid] == item):
            return mid
        elif (arr[mid] > item):
            high = mid - 1
        else:
            low = mid + 1
    return None


arr = [-10, -5, 1, 2, 3, 4, 5]
item = 3
index = binary_search(arr, item)
print(index)
