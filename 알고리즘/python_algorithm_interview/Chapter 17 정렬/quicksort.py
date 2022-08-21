# quicksort
# 2022-08-21

def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
        A[left], A[hi] = A[hi], A[left]
        return left
    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, pivot + 1, hi)