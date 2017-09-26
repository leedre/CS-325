'''
Jon-Eric Cook
CS-325
Homework #1
This program demonstrates the merger sort algorithm. It does this by opening
a file named data.txt, reading in data, sorting said data via the merge sort
algorithm and then outputing the results to a file named merge.out.
'''

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

# open the input file
input_file = open('data.txt','r')

# create the output file
output_file = open('merge.out','w')

# convert the string to a array of characters
line = input_file.readline().split(' ')
while line != ['']:
    # convert to an array of integers
    line = map(int, line)

    # discard the first number
    line = line[1:]

    # call mergesort
    s = mergesort(line)

    # output the sorted array to the output file
    output_file.write(' '.join(map(str,s)))
    output_file.write('\n')

    # get another line
    line = input_file.readline().split(' ')

# close the files
input_file.close()
output_file.close()


# RESOURCES:
# The below links were used to help me complete this problem
# I spent 5 hours on this problem.
# Please see the screen shots of my debugging as I did my best to fully
# understand how the recursion worked.
# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/
# https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
# http://mooreccac.com/kcppdoc/Recursion.htm
