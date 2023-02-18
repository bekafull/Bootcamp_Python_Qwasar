def my_array_uniq(param_1):
    x = []
    for i in param_1:
        if i not in x:
            x.append(i)
    return x
    