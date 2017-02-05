from collections import defaultdict

def solution(H):

    bar_counter = defaultdict(int)
    stack = [(0,0)]
    total = len(H)
    for i, key in enumerate(H):
        bar_counter[key] += 1
        while key < stack[-1][0]:
            poped = stack.pop()
            total += min(-bar_counter[poped[0]] + 1, 0)
            bar_counter[poped[0]] = 0

        if key > stack[-1][0]:
            stack.append((key, i))
    else:
        for val in bar_counter.values():
            total += min(-val + 1, 0)
    return total
