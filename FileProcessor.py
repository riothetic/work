import os, os.path


#----- counting files in the renamed directory -----#

ids = len(os.listdir('./results/renamed/'))

n = 0
participantid = []

while n < ids:
    n = n + 1
    m = n + 10
    participantid.append(m)


# filtering the files for videoname and rating
print participantid


def FilterLogs(participantid):

    print('filtering...')


    for idx in participantid:
        infile = file('./results/renamed/%s.txt' % idx, 'r')
        outfile = file('./results/filtered/%s.txt' % idx, 'w')
        videos = []
        ratings = []
        results = []


        for idx,line in enumerate(infile):
            values = line.strip().split(',')
            videos.append(values[1])
            ratings.append(values[2])
            outfile.write('%s,%s\n' % (videos[idx],ratings[idx]))


    print('filtering successful')


#----- sorting the files by videoname -----#

def SortLogs(participantid):

    print('sorting...')


    for num in participantid:
        infile = file('./results/filtered/%s.txt' % num, 'r')
        outfile = file('./results/sorted/%s.txt' % num, 'w')

        xlist = []


        for line in infile:
            xlist.append(line)


        xlist.pop(0)
        sortedxlist = sorted(xlist)


        for idx, element in enumerate(sortedxlist):
            outfile.write(sortedxlist[idx])


    print('sorting successful')


#----- joining the actions (2 separate files before) -----#

def master():
    FilterLogs(participantid)
    SortLogs(participantid)


master()
