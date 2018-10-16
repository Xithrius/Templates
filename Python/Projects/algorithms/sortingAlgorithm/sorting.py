def bubble(l):  # n^2
    l = list(l)  # Copy l

    # EXAMPLE
    # [3, 2, 5, 0, 1]
    # [2, 3, 0, 1, 5]
    # [2, 0, 1, 3, 5]
    # [0, 1, 2, 3, 5]
    # [0, 1, 2, 3, 5]

    swapped = True  # was there a swap on last 'pass'?

    while swapped:  # While changes are being made
        swapped = False  # no swaps have occurred
        for i in range(len(l) - 1):  # iterate through indices of list
            if l[i + 1] < l[i]:  # swap
                l[i], l[i + 1] = l[i + 1], l[i]  # switches elements
                swapped = True  # more work may need to be done

    return l


def mergesort(l):  # n*ln(n)
    # [3, 2, 5, 0, 1]
    # [3, 2] [5, 0, 1]
    # [3] [2] [5] [0, 1]
    # [2, 3] [5] [0] [1]
    # [2, 3] [5] [0, 1]
    # [2, 3] [0, 1, 5]
    # [0, 1, 2, 3, 5]
    l = list(l)
    if len(l) <= 1:
        return l

    return merge(mergesort(l[:len(l) // 2]), mergesort(l[len(l) // 2:]))


def merge(l0, l1):
    newList = []

    while len(l0) > 0 and len(l1) > 0:
        if l0[0] < l1[0]:
            newList.append(l0.pop(0))
        else:
            newList.append(l1.pop(0))

    newList += l0 + l1

    return newList


print(mergesort([3, 2, 5, 0, 1]))
