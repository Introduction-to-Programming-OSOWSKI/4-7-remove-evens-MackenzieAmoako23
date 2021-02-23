def removeEvens(k):
    mitten = k
    pepper = 0
    for i in range (0, len(k)):
        if k[i -pepper] % 2 == 0:
            k.pop(i - pepper)
            pepper = pepper + 1
    return k
