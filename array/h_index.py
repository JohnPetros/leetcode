def h_index(citations: list[int]) -> int:
    n = len(citations)
    paper_counts = [0] * (n + 1)

    for index in range(n):
        citation = citations[index]
        if citation >= n:
            paper_counts[-1] += 1
        else:
            paper_counts[citation] += 1
    h = n
    max_paper_count = paper_counts[n]
    while max_paper_count < h:
        h -= 1
        max_paper_count += paper_counts[h]

    return h
    # Time: O(n)
    # Space: O(n)


print(h_index([5, 1, 2, 8, 9, 3]))
