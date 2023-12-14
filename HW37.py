def first(size, *args):
    sum = size + len(args)
    return sum
    


def second(size, **kwargs):
    sum = size + len(kwargs)
    return sum