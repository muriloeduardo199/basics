def soma(*args):
    total = 0
    for numero in args:
        total+= numero
    return total
soma1=(1,2,3,4,444,444)


print(soma(*soma1)) 