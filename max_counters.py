def solution(N, A):

    counters = N * [0]

    max_counter = 0

    next_max_counter = 0

    for oper in A:
        if oper <= N:
            current = counters[oper-1] = max(counters[oper-1] +1, max_counter+1)

            next_max_counter = max(current, next_max_counter)
        else:
            max_counter = next_max_counter

    return [c if c > max_counter else max_counter for c in counters]
