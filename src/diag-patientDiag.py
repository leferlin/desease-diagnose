import csv
import diag


f = open('Diagnose.csv', "r")
lines = f.read().split("\n") # "\r\n" if needed

title = lines[0]

# Create Person table
with open('PatientDiagnose.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['pacientID', 'diagnoseID'])

    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(",")
            patientID = 'pat'+diag.id_generator()
            diagnoseID = values[0]

            spamwriter.writerow([patientID, diagnoseID])

f.close()
