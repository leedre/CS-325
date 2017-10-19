'''
Jon-Eric Cook
CS-325
Homework #4
This program demonstrates a greedy algorithm. It does this by selecting
the last activity to start that is compatible with all previously selected
activities.
'''

# merge algorithm
def merge(l,r):
    # empty array to be used to hold sorted values
    s = []
    # append to s array until either l or r array is empty
    while len(l) != 0 and len(r) != 0:
        if l[0][1] > r[0][1]:
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

# selects non conflicting activites from a list
def select_acts(a):
    n = len(a)
    sa = [a[0]]
    k = 0
    for m in range(1,n):
        if a[m][2] <= sa[k][1]:
            sa.append(a[m])
            k += 1
    return sa

# opens the act file for reading
input_file = open('act.txt','r')
set_count = 0

# loops until the end of the act file is reached
while True:
    # gets a line from the file
    line = input_file.readline()
    # removes any spaces at the beginning or end of the line
    line = line.strip()
    # turn the line into a list
    line = line.split(' ')
    # if the end of file is reached, break
    if line == ['']:
        break
    # turn the list of strings into a list of integers
    line = map(int,line)
    if len(line) == 1:
        set_count += 1
        counter = line[0]
        acts = []
    # loop for the number of activities in the set
    for i in range(0,counter):
        line = input_file.readline()
        line = line.strip()
        line = line.split(' ')
        line = map(int,line)
        # create list of activities
        act = [line[0],line[1],line[2]]
        # put in list, to create a list of lists
        acts.append(act)
    # sort the list of lists
    sorted_acts = mergesort(acts)
    # select all activities that dont conflict
    selected_acts = select_acts(sorted_acts)

    # print results
    print "Set", set_count
    print "Number of activities selected =", len(selected_acts)
    g = "Activities:"
    for i in reversed(range(0,len(selected_acts))):
        g = g + " " + str(selected_acts[i][0])
    print g
    print "\n"

input_file.close()
