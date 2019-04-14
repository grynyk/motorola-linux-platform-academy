def append_func(*args):
    result = []
    for arg in args:
        if type(arg) == list:
            for i in arg:
                result.append(i)
        else:
            result.append(arg)
    return result

print(append_func(1,[2,3,3,4,5],2,3,4,[1,2,3]))
