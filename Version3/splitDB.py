import csv



def divide_file_70_30(reader):
    local_db70 = []
    local_db30 = []
    reader = list(reader)
    rows70 = round(len(list(reader)) * 0.7)  # Find 70% of rows in CSV
    count = 0
    for i in reader:
        #print(i)
        if count <= rows70:
            local_db70.append(i)  # input 70% of file to local_db variable
            count += 1
        else:
            local_db30.append(i)  # input 30% of file to local_db30 variable
            #print(i)
            count += 1
    return local_db70, local_db30


# Open CSV File

