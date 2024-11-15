def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 테스트
array = [64, 34, 25, 12, 22, 11, 90]
print("버블 정렬 결과:", bubble_sort(array))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 테스트
array = [64, 34, 25, 12, 22, 11, 90]
print("퀵 정렬 결과:", quick_sort(array))
