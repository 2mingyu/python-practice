# Merge Sort 구현
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 중간 지점
        left_half = arr[:mid]
        right_half = arr[mid:]

        # 재귀적으로 나누기
        merge_sort(left_half)
        merge_sort(right_half)

        # 병합 과정
        i = j = k = 0
        
        # 두 하위 배열을 병합
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 요소 처리
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Quick Sort 구현
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 피봇 선택
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# 테스트용 배열
arr_merge = [38, 27, 43, 3, 9, 82, 10]
arr_quick = [38, 27, 43, 3, 9, 82, 10]

print("Merge Sort 전: ", arr_merge)
merge_sort(arr_merge)
print("Merge Sort 후: ", arr_merge)

print("\nQuick Sort 전: ", arr_quick)
arr_quick_sorted = quick_sort(arr_quick)  # Quick Sort는 새로운 배열을 반환함
print("Quick Sort 후: ", arr_quick_sorted)
