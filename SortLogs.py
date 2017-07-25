import os, os.path

# counting files in the renamed directory
ids = len(os.listdir('./results/filtered/'))

n = 0
participantid = []

while n < ids:
    n = n + 1
    m = n + 10
    participantid.append(m)


# filtering the files for videoname and rating
print participantid

for num in participantid:
    infile = file('./results/filtered/%s.txt' % num, 'r')
    outfile = file('./results/sorted/%s.txt' % num, 'w')

    xlist = []

    for line in infile:
        xlist.append(line)

    del xlist[1]

    sortedxlist = sorted(xlist)

    for idx, element in enumerate(sortedxlist):
        outfile.write(sortedxlist[idx])
