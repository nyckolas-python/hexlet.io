def does_contain(text, symbol):
    i = 0
    while i < len(text):
        if text[i] == symbol:
            return True
        i += 1
    return False