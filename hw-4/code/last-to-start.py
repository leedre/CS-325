'''
Jon-Eric Cook
CS-325
Homework #4
This program demonstrates a greedy algorithm. It does this by selecting
the last activity to start that is compatible with all previously selected
activities.
'''

input_file = open('act.txt','r')
activities = []
while True:
    line = input_file.readline()
    line = line.strip()
    line = line.split(' ')
    if line == ['']:
        break
    line = map(int, line)
    if len(line) == 1:
        numb_act = line[0]
        activities.append(numb_act)
    else:
        activity = {'start':line[1],'finish':line[2],'id': line[0]}
        activities.append(activity)

for i in range(0,len(activities)):
    print activities[i]

input_file.close()
