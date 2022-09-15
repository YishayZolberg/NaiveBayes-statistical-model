import csv
def csv_data():
    local_db = []

    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader: #make a data base of arrays
            local_db.append(row)

    return local_db

def make_unique(local_db):
    unique_vals = {}
    titles = local_db.pop(0)

    for num, row in enumerate(local_db):
        print(num,row)
        for number, col in enumerate(row):
            unique_vals[titles[number]] = {}
            # if col not in unique_vals[titles[number]]:
            #     unique_vals[titles[number]].setdefault(col,' ')
    #print(unique_vals)
    for number, col in enumerate(local_db[number]):
            for num, row in enumerate(local_db):
                # if row[number] not in unique_vals[titles[number]]:
                #
                unique_vals[titles[number]] |= { col : ' ' }
    #print(unique_vals)



global_db = csv_data()
make_unique(global_db)
