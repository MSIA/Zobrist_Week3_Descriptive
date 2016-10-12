from os import listdir
import csv

mypath = 'T:courses/MSiA400/jobs/job_descriptions'
files = [f for f in listdir(mypath) if f[-12:] == '_expired.csv']
fout = open('out.csv','w')
w = csv.writer(fout)

w.writerow(['GUID','DateExpired'])

for i in files:
    with open(i) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            w.writerow(row)

fout.close()


