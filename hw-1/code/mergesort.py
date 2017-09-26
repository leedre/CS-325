input_file = open('data.txt','r')
line = input_file.readline().split(' ')
while line != ['']:
    line = map(int, line)
    length = line[0]
    line = line[1:]
    print length
    print line
    line = input_file.readline().split(' ')

input_file.close()
