def solution(S, P, Q):
    trans = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    S = [trans[s] for s in S]

    s_tree = MinBTree(S)

    output = []
    for p, q in zip(P, Q):
        output.append(s_tree.query(p, q))


    return output
