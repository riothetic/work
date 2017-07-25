#----- importing stuff -----#

import numpy as np
import csv
import os, os.path


#----- declaring variables/lists -----#

main_list = []                                                                          # list of lists with all the videoratings per person
#rating_list = []                                                                       # variable for the lists inside main_list
name_list = []                                                                          # list with all the videonames
mean_list = []
participant_mean_list = []
video_mean_list = []
n = 0
participant_id_list = []                                                                      # list of partipant id's
c = 0


#----- counting files and makin a list of filenumbers (participant-id's) -----#

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


'''

#----- writing the video names into the first csv column -----#

main_outfile.write('Videoname\n')
for e in name_list:
    main_outfile.write('%s\n' % e)





with open('./results/Spreadsheet.csv', 'rw') as file:

    file.write()

    for idx,row in enumerate(reader):
        if row[0] == 'Videoname':
            pass
        else:
            writer.writerow(row+[videoname[idx -1]])




    #for name in name_list:
        #writer.writerow(row + name)


#----- writing the overall mean per video into the second csv column-----#

with open('./results/Spreadsheet.csv', 'rw') as file:

    reader = csv.reader(file)
    writer = csv.writer(file, delimiter=',')

    for idx,row in enumerate(reader):

        if row[0] == 'Videoname':
            writer.writerow(row+['Mean'])
        else:
            rating_list = np.array(main_list[idx -1]).astype(np.float)
            arithm = np.mean(rating_list)
            writer.writerow(row+[arithm])


    for rating_list in main_list:
        rating_list = np.array(rating_list).astype(np.float)
        arithm = np.mean(rating_list)
        print(arithm)
        writer.writerow(arithm)

'''
