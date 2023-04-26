def binary_search(array, n):
    cur = len(array) // 2
    if array[cur] == n:
        return cur
    elif array[cur] > n:
        return binary_search(array[:cur], n, doprint)
    else:
        return binary_search(array[(cur + 1):], n, doprint)


binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)
