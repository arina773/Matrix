def solution(A):
    min_h = 1
    len_a = len(A)
    max_h = len_a
    while min_h < max_h:
        avarage = (1 + max_h + min_h) // 2
        i = 0
        while i < len_a:
            j = i
            while j < len_a and A[j] >= avarage:
                j += 1
            if j - i >= avarage:
                min_h = avarage
            i = max(j, i + 1)
        max_h = avarage - 1
    return min_h 
