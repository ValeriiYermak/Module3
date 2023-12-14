def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        # j = (length - len(string)) // 2
        # i = " " * j
        # string = i + string
        string = " " * ((length - len(string)) // 2) + string
        return string
    

    string = " " * (length - len(string)) // 2 + string