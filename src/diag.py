import csv
import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))

def date_generator(firstYear, lastYear):
    year = str(random.randint(firstYear, lastYear))
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)
    return day+'/'+month+'/'+year


f = open('diag-db.csv', "r")
lines = f.read().split("\n") # "\r\n" if needed

title = lines[0]

# Create Desease table
with open('Desease.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['code', 'symptom'])

    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(',')
            desease = values[0].split('^')[0]

            if desease != '':
                deseaseCode = desease.split('_')[0]
                deseaseName = desease.split('_')[1]
                spamwriter.writerow([deseaseCode, deseaseName])


# Create Symptoms table
with open('Symptom.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['code', 'symptom'])
    symptoms = {}

    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(',')
            symptom = values[2].split('^')[0]
            symptomCode = symptom.split('_')[0]
            symptomName = symptom.split('_')[1]

            if not symptomCode in symptoms:
                symptoms[symptomCode] = symptomName
                spamwriter.writerow([symptomCode, symptomName])

# Create DeseaseSymptoms table
with open('DeseaseSymptoms.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['deseaseCode', 'symptomCode'])
    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(",")

            if values[0] != '':
                lastDesease = values[0].split('_')[0]
            symptom = values[2].split('_')[0]
            spamwriter.writerow([lastDesease, symptom])


# Create Diagnose table
with open('Diagnose.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['personID', 'codeDisease'])

    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(",")

            if values[0] != '':
                times = int(values[1])

                for i in range(0, times):
                    ID = 'diag'+id_generator()
                    codeDesease = values[0].split('_')[0]
                    date = date_generator(2004, 2004)
                    spamwriter.writerow([ID, codeDesease, date])

# end
