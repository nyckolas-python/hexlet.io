def is_continuous_sequence(a):
    if len(a) > 1:
        n = a[1] - a[2]
        for i in range(len(a) - 1):
            if (a[i] - a[i + 1]) != n:
                return False
                break
        return True
    else:
        return False