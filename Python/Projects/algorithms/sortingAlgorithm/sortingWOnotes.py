def bubble(l):
    l = list(l)
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(l) - 1):
            if l[i + 1] < l[i]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swapped = True
    return l


def mergesort(l):
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
