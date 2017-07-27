#----- importing stuff -----#

import numpy as np
import csv
import os, os.path
import matplotlib.pyplot as plt


#----- declaring variables/lists -----#

main_list = []                  # list of lists with all the videoratings per person((4,5,2,4,...)(3,4,2,5,...))
name_list = []                  # list with all the videonames (video_hc023.mp4, ...)
participant_mean_list = []      # arithmetic mean per participant
video_mean_list = []            # arithmetic mean per video
participant_id_list = []        # list of partipant id's (11,12,13,14,...)

c = 0
n = 0


#----- counting files and making a list of filenumbers (participant-id's) -----#

ids = len(os.listdir('./results/sorted/'))

while n < ids:
    n = n + 1
    m = n + 10
    participant_id_list.append(m)


#----- processing the files into python lists -----#

for f in participant_id_list:

    infile = file('./results/sorted/%s.txt' % f, 'r')
    tmp_rating_list = []
    c = c + 1


    for line in infile:

        tmp_list = []
        tmp_list2 = []
        tmp_list3 = []
        tmp_list = line.strip().split(',')

        tmp_list2 = list(tmp_list)
        tmp_list.pop(0)
        v = tmp_list[0]
        int(v)
        tmp_rating_list.append(v)


        if c == 1:

            tmp_list3 = list(tmp_list2)
            tmp_list3.pop(1)
            n = tmp_list3[0]
            name_list.append(n)


    main_list.append(tmp_rating_list)


#----- calculating mean per person -----#

for tmp_rating_person_list in main_list:

    tmp_rating = np.array(tmp_rating_person_list).astype(np.float)
    arithm = np.mean(tmp_rating)
    participant_mean_list.append(arithm)


#----- calculating mean per video -----#

for idx,videoname in enumerate(name_list):

    tmp_rating_list2 = []


    for l in main_list:

        tmp_rating_list2.append(float(l[idx]))


    arithm = np.mean(tmp_rating_list2)
    video_mean_list.append(arithm)


#----- spreadsheet: videoname / video mean / participant ratings(full) -----#

with open('./results/Spreadsheet_videoname.csv', 'w') as spreadsheet_file:

    spreadsheet_writer = csv.writer(spreadsheet_file)
    spreadsheet_writer.writerow(['Videoname'] + ['Mean'] + participant_id_list)


    for idx,e in enumerate(name_list):

        tmp_video_rating_list = [value[idx] for value in main_list]
        spreadsheet_writer.writerow([e] + [video_mean_list[idx]] + tmp_video_rating_list)


#----- spreadsheet: participant id / Mean / correlation -----#

with open('./results/Spreadsheet_person.csv', 'w') as spreadsheet_file:

    spreadsheet_writer = csv.writer(spreadsheet_file)
    spreadsheet_writer.writerow(['Participant ID'] + ['Mean'] + ['Correlation'])


    for idx,e in enumerate(participant_id_list):

        corrx = main_list[idx]
        corry = video_mean_list
        corr = np.corrcoef(corrx, corry)
        spreadsheet_writer.writerow([e] + [participant_mean_list[idx]] + [corr[0][1]])
