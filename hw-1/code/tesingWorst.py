# turns a sorted array into the worst order for merge sort
def worst(a):

    if len(a) <= 1:
        return a
    if len(a) == 2:
        temp = a[0]
        a[0] = a[1]
        a[1] = temp
        return a

    mid = (len(a) + 1) / 2
    l = []
    r = []

    i = 0
    j = 0
    while i < len(a):
        l.append(a[i])
        i += 2
        j += 1

    i = 1
    j = 0
    while i < len(a):
        r.append(a[i])
        i += 2
        j += 1

    f = worst(l)
    g = worst(r)
    b = f + g
    return b

# sorted array
sorted_list = range(8)
print sorted_list

# get the worst order for the array
worst_list = worst(sorted_list)
print worst_list
