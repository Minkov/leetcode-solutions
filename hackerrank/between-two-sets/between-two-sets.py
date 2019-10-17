
def getTotalX(a, b):
    f = max(a)
    m = min(b)
    count = 0
    for i in range(f, m + 1):
        is_in_between = True
        for x in a:
            if i % x > 0:
                is_in_between = False
                break
        for x in b:
            if x % i > 0:
                is_in_between = False
                break
        if is_in_between:
            count += 1
    return count


print(getTotalX([2, 4], [16, 32, 96]))