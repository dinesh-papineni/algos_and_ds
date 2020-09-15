# Sort an array using quick sort recursively
def quick_sort_recursion(arr):
    if (len(arr) < 2):
        return arr
    else:
        # choose pivot at middle of array to avoid worst case run time
        low = 0
        high = len(arr) - 1
        pivot = arr[(low + high) // 2]
        # Can also choose first element as pivot
        # pivot = arr[0]
        smaller = [i for i in arr if i < pivot]
        larger = [i for i in arr if i > pivot]
        return quick_sort_recursion(smaller) + [pivot] + quick_sort_recursion(larger)


arr = [-10, -5, 1, 2, 3, 4, 5]
sorted_arr = quick_sort_recursion(arr)
print(sorted_arr)
