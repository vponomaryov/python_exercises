import random
import timeit


# === Quick sorting ===
def _quick_sort(list_, start, end):
    li, ri = start, end
    pivot = list_[(start + end) // 2]

    while li <= ri:
        while list_[li] < pivot:
            li += 1
        while list_[ri] > pivot:
            ri -= 1
        if li <= ri:
            list_[ri], list_[li] = list_[li], list_[ri]
            li += 1
            ri -= 1

    if start < ri:
        _quick_sort(list_, start, ri)
    if li < end:
        _quick_sort(list_, li, end)
    return list_


def quick_sort(list_):
    return _quick_sort(list_, 0, len(list_) - 1)


# === Bubble sorting ===
def bubble_sort(list_):
    list_len = len(list_)
    if list_len < 2:
        return list_
    while list_len:
        for i in range(list_len - 1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
        list_len -= 1
    return list_


# ======= Run sorting operations =======
results = []
sort_me = random.sample(range(10, 100), 40)
print("Original data: %s\n" % sort_me)
for sort_info in (
        (bubble_sort, 'Custom bubble sort'),
        (quick_sort, 'Custom quick sort'),
        (sorted, 'Built-in sort')):
    start = timeit.default_timer()
    results.append(sort_info[0](sort_me))
    stop = timeit.default_timer()
    print("%s time: %s" % (sort_info[1], stop - start))
print("\nAll three sort operations provided equal data: %s" % (
    results.count(results[0]) == len(results)))
