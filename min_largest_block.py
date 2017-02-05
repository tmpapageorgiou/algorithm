def solution(K, M, A):
    N = len(A)

    min_largest_sum = max(A)
    max_largest_sum = sum(A)

    if K == 1:
        return max_largest_sum

    if K == len(A):
        return min_largest_sum

    while min_largest_sum <= max_largest_sum:
        largest_sum = (min_largest_sum + max_largest_sum)/2

        acumulator = 0
        k_counter = 1
        for val in A:
            acumulator += val

            if acumulator > largest_sum:
                acumulator = val
                k_counter += 1
                if k_counter > K:
                    break

        if k_counter <= K:
            max_largest_sum = largest_sum - 1
            result = largest_sum
        else:
            min_largest_sum = largest_sum + 1

    return result
