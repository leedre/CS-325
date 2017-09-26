def merge(l,r):
    s = []
    while len(l) != 0 and len(r) != 0:
        if l[0] < r[0]:
            s.append(l[0])
            l.remove(l[0])
        else:
            s.append(r[0])
            r.remove(r[0])
    if len(l) == 0:
        s += r
    else:
        s += l
    return s

def mergesort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a)/2
        l = mergesort(a[:mid])
        r = mergesort(a[mid:])
        return merge(l,r)

input_file = open('data.txt','r')
output_file = open('merge.out','w')
line = input_file.readline().split(' ')
while line != ['']:
    line = map(int, line)
    line = line[1:]
    s = mergesort(line)
    output_file.write(' '.join(map(str,s)))
    output_file.write('\n')
    line = input_file.readline().split(' ')

input_file.close()
output_file.close()

# https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/tutorial/
# https://pythonandr.com/2015/07/05/the-merge-sort-python-code/
