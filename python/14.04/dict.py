def dict_without_nones(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if value is not None:
            result[key] = value
    print(result)
    dict_without_nones_c(**kwargs)

def dict_without_nones_c(**kwargs):
    result2 = {
        arg[0]:arg[1] for arg in kwargs.items()
        if arg[1] is not None
    }
    print(result2)

dict_without_nones(a=2,b=3,c=None,d=4,f=None)
