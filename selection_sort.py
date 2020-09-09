# Selction Sort
def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if(arr[j] < arr[min_index]):
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

  return

arr = [2, 5, 1, -12, 3000, 4, -9, 3, 5]

print(f'Original Array: {arr}')
selection_sort(arr)
print(f'Sorted Array: {arr}')
