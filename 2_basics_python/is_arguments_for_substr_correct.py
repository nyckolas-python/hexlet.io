def is_arguments_for_substr_correct(string, start, length):
    if length < 0 or start < 0 or start > (len(string) - 1) or (start + length) > len(string):
        return False
    else: return True