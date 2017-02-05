def solution(A, B):

    stack = []
    total = 0
    for size, downstream in zip(A, B):

        if not downstream:
            while stack and stack[-1] < size:
                stack.pop()
            if not stack:
                total += 1

        if downstream:
            stack.append(size)

    return total + len(stack)
