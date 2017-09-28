'''
Jon-Eric Cook
CS-325
Homework #1
This program compares the experimental running times of the merger sort
algorithm for the best and worst array inputs.
'''
import timeit

# wrapper function
def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# merge algorithm
def merge(l,r):
    # empty array to be used to hold sorted values
    s = []
    # append to s array until either l or r array is empty
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            s.append(l[0])
            l.remove(l[0])
        else:
            s.append(r[0])
            r.remove(r[0])
    # add the remaining value to the s array
    if len(l) == 0:
        s += r
    else:
        s += l
    return s

# mergesort algorithm
def mergesort(a):
    # if the array has only one element, return it
    if len(a) == 1:
        return a
    else:
        # call mergesort on half of the current input array
        mid = len(a)/2
        l = mergesort(a[:mid])
        r = mergesort(a[mid:])
        return merge(l,r)

# turns a sorted array into the worst order for merge sort
def worst(a):
    # return the array if is 1 or less elements
    if len(a) <= 1:
        return a
    # swap the elements
    if len(a) == 2:
        temp = a[0]
        a[0] = a[1]
        a[1] = temp
        return a
    # get the mid point
    mid = (len(a) + 1) / 2
    # left and right arrays
    l = []
    r = []
    # split up the array into left part
    i = 0
    j = 0
    while i < len(a):
        l.append(a[i])
        i += 2
        j += 1
    # split up the array into right part
    i = 1
    j = 0
    while i < len(a):
        r.append(a[i])
        i += 2
        j += 1
    # keep breaking the array down
    f = worst(l)
    g = worst(r)
    # combine the two parts
    b = f + g
    return b

# arrays to hold times from merge sort function
mergesort_data_best = []
mergesort_data_worst = []

# number of elements to be in random array
elements = [1000,2000,4000,8000,16000,32000,64000]

# loop 7 times, timing the run time of the merge sort algorithm for 7 different
# array sizes, best and worst types
for x in range(7):
    # best order
    best_list = range(elements[x])
    # worst order
    worst_list = worst(best_list)

    # wrap mergesort function
    wrapped = wrapper(mergesort, best_list)
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for mergesort
    n = "n = "
    n += str(elements[x])
    mergesort_data_best.append(n)
    sec = "sec = "
    sec += str(time_taken)
    mergesort_data_best.append(sec)

    # wrap mergesort function
    wrapped = wrapper(mergesort, worst_list)
    # time mergesort function
    time_taken = timeit.timeit(wrapped, number=1)

    # log number of elements and time taken for mergesort
    n = "n = "
    n += str(elements[x])
    mergesort_data_worst.append(n)
    sec = "sec = "
    sec += str(time_taken)
    mergesort_data_worst.append(sec)

print "Merge Sort - best"
print mergesort_data_best

print "Merge Sort - worst"
print mergesort_data_worst



# RESOURCES:
# The below link was used to help me complete this problem.
# http://pythoncentral.io/time-a-python-function/
# https://stackoverflow.com/questions/24594112/when-will-the-worst-case-of-merge-sort-occur
