# Sort an array using quick sort recursively
def quick_sort_recursion(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        smaller, larger = [], []
        for i in arr[1:]:
            if i <= pivot:
                smaller.append(i)
            else:
                larger.append(i)
        return quick_sort_recursion(smaller) + [
            pivot
        ] + quick_sort_recursion(larger)


arr = [-10, -5, 1, 2, 3, -10, 4, 5]
sorted_arr = quick_sort_recursion(arr)
print(sorted_arr)

