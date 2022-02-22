def rotated_left(list):
    list = list[1:] + list[:1]
    return list
def rotated_rigth(list):
    list = list[-1:] + list[:-1]
    return list