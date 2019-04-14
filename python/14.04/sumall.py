def sumall(*args):
    try:
        if len(args) == 0:
            raise ValueError('No args')
        sum = 0
        for arg in args:
            sum +=arg
        return sum

print(sumall())