def filter_string(text, symbol):
    string_new = ''
    i = 0
    while i < len(text):
        if text[i] != symbol:
            string_new += text[i]
        i += 1
    return string_new