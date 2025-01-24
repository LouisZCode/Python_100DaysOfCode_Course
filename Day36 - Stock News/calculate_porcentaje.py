def calculate_porcentage(val1, val2):
    n1 = val1
    n2 = val2

    dif = n1 - n2
    ave = (n1 + n2)/2
    ratio = (dif / ave) * 100

    absolute = int(abs(ratio))

    return absolute
