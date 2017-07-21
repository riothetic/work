# plotting the data

import matplotlib.pyplot as plt
import numpy as np
import os, os.path



# counting files in the renamed directory
ids = len(os.listdir('./results/sorted/'))


n = 0
participantid = []

while n < ids:
    n = n + 1
    m = n + 10
    participantid.append(m)

# creating an index list for the videonames


n = 1
videonumber = []

while n <= 166:
    videonumber.append(n)
    n = n + 1


# reading files into a list with index for histogram (sorted by index)

for f in participantid:

    infile = file('./results/sorted/%s.txt' % f, 'r')

    rating = []

    for line in infile:

        list1 = []
        list1 = line.strip().split(',')
        list1.pop(0)
        value = list1[0]
        int(value)

        rating.append(value)

    numrow = len(participantid)
    num = int(f) - 10


    plt.figure(1)
    plt.subplot(numrow, 1, num)
    plt.plot(rating, 'bo')
    plt.ylabel('rating')
    plt.xlabel('video id')
    plt.title(f)

plt.show()



# reading files into a list sorted by rating with index
