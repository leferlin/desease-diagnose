import csv
import names
import diag
import random

def sex_generator():
    sex = random.randint(0,1)
    if sex == 0:
        return 'M'
    return 'F'

def phone_generator():
    return random.randint(8000000, 9999999)

def locality_generator():
    direction = random.randint(1,8)
    if direction == 1:
        return 'North'
    elif direction == 2:
        return 'South'
    elif direction == 3:
        return 'East'
    elif direction == 4:
        return 'West'
    elif direction == 5:
        return 'Northeast'
    elif direction == 6:
        return 'Southeast'
    elif direction == 7:
        return 'Southwest '
    elif direction == 8:
        return 'Northwest'



f = open('PatientDiagnose.csv', "r")
lines = f.read().split("\n") # "\r\n" if needed

title = lines[0]

# Create Person table
with open('Patient.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['ID', 'name', 'birth', 'phone', 'locality'])

    for line in lines:
        if line != '' and line != title: # add other needed checks to skip titles
            values = line.split(",")
            ID = values[0]
            sex = sex_generator()
            if sex == 'M':
                name = names.get_full_name(gender='male')
            else:
                name = names.get_full_name(gender='female')

            birth = diag.date_generator(1900,2003)
            phone = phone_generator()

            locality = locality_generator()

            codeDesease = values[0].split('_')[0]
            spamwriter.writerow([ID, name, birth, phone, locality])

f.close()
