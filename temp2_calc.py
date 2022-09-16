import csv
import copy

def csv_data():
    local_db = []
# TO DO : make a check to verify we dont enter empty lines to the local db OR enpty file OR nonexistant file
    with open('db.csv') as db:
        reader = csv.reader(db, delimiter=',')
        for row in reader: #make a data base of lists
            local_db.append(row)

    return local_db

#this function deletes the titles of the csv and puts them in a list.
def exp_titles(local_db):
    titles = []
    titles = local_db.pop(0)
    return titles

#this function makes the titles of the csv into dictionary keys and the values are the unique options of each column (first and seconed layer of model)
def make_unique(local_db):
    unique_vals = {}
    temp_list = []
    temp_list1 = []

    titles = exp_titles(local_db) #calling the function who deletes the titles and puts them in a list.
    unique_vals = dict.fromkeys(titles, ' ') #converting the titles into keys and inserting them in the data model dictionary.

    for number in range(len(local_db[0])):
        for num, row in enumerate(local_db):
            temp_list.append(local_db[num][number]) #putting the values of the entire column in a list
        for i, key in enumerate(unique_vals):
            if i == number:
                temp_list1 = set(temp_list) #making the column a set in order to make values unique and then changing the type back to dictionary
                unique_vals[key] = dict.fromkeys(temp_list1, ' ')
        temp_list.clear()
    return unique_vals, titles

#this function gets the database, a boolian value with the user's question column choice and the data models,
#and returns a dictionary w the unique options of values from the chosen column, and the column's title.
def choice_question(local_db,titles,unique_vals):
    #here we would have the user input the choice of classification column:
    choice = False
    # true for first column and false for last column
    ques_col = []
    ques_col_set = []
    choice_title = ' '

    for number in range(len(local_db[0])):
        for num, row in enumerate(local_db):
            if choice == True and number == 0:
                ques_col.append(local_db[num][number])
                ques_col_set = set(ques_col)
                choice_title = titles[0]


            elif choice == False and number == (len(row)-1) :
                ques_col.append(local_db[num][number])
                ques_col_set = set(ques_col)
                choice_title = titles[-1]

    del unique_vals[choice_title] #we want to delete the choice column key for the count we will do later
    dict_corl = dict.fromkeys(ques_col_set, 0) #we want to make the options set into a dictionary
    return dict_corl, choice_title

#this function inserts the third layes of the data model: the unique options of the question column
def count_set_up(unique_vals, dict_corl):
    temp = {}
    for key, value in unique_vals.items():
        temp = dict.fromkeys(value, ' ')

        for value2 in value:
            dict_corl1 = copy.deepcopy(dict_corl)
            temp[value2] = dict_corl1
        unique_vals[key]=temp

    return unique_vals


#the function counts all of the unique instances of matches with the question column.
def count_corolation(unique_vals, dict_corl, local_db, choice_title, titles):
    lst = []
    indx = 0
    len1 = len(local_db[0]) - 1
    key_num = ''

    unique_vals = count_set_up(unique_vals, dict_corl) #setting up the model for the count

    #putting the choices of the question column in a list
    for y_s in dict_corl.keys():
        dict_corl[y_s] = 0
        lst.append(y_s)


    #deleting the title of the choice column out of the titles list.
    indx= titles.index(choice_title)
    del titles[indx]

    #iterating over the columns of the data base and checking if it matches the options of the question column.
    for number in range(len(local_db[0])):
        for num, row in enumerate(local_db):
            if number <= len(titles)-1 and unique_vals[titles[number]].get(row[number], None) != None:
                if row[len1] == lst[0]: #if is no
                    unique_vals[titles[number]][row[number]][lst[0]] += 1
                elif row[len1] == lst[1]: #if is yes
                    unique_vals[titles[number]][row[number]][lst[1]] += 1

            elif row[number] == lst[0]: #also counting the options of the
                dict_corl[lst[0]] += 1
            elif row[number] == lst[1]:
                dict_corl[lst[1]] += 1

    print(unique_vals)
    print(dict_corl)

def class_main():
    local_db = []
    unique_vals = {}
    dict_corl = {}
    choice_title = ''

    local_db = csv_data() #create data base
    unique_vals, titles = make_unique(local_db) #return two data models
    dict_corl, choice_title = choice_question(local_db, titles, unique_vals) #return the relevant info from the user's choice
    count_corolation(unique_vals, dict_corl, local_db, choice_title, titles)

class_main()

