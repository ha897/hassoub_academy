from csv import writer
from flask import  jsonify, current_app
import os, sqlite3, openpyxl
from faker import Faker
import pandas as pd
from tabulate import tabulate
import numpy as np

#create an array from html page
def html_to_array(weburl, tablenum):

    # read tables from html page
    url = weburl 
    tables = pd.read_html(url)

    # indexing start with 1
    try:
        table = tables[tablenum - 1]
    except IndexError:
        return 'error: table number out of range.'
    

    # create array
    htmlarray = np.array(table)

    return htmlarray
            

# delete unicode
def delete_unicode(htmlarray):  
    for items in range(len(htmlarray)):
        for item in range(len(htmlarray[items])):
            for char in range(len(htmlarray[items])):
                if htmlarray[items][char] == ' ' or type(htmlarray[items][char]) != str:
                    pass
                elif (lambda lamdaitem: any(ord(lamdaitem) > 127 for lamdaitem in htmlarray[items][char]))(htmlarray[items][char]):
                    if type(htmlarray[items][item]) == str: 
                         htmlarray[items][item] = htmlarray[items][item].encode('utf-8')           

    return htmlarray

            


def chacke_filename_extantion(filename, filetype):
    if filename.endswith("." + filetype):
        return filename
    else:
        if filename.rfind(".") == -1:
            return filename + "." + filetype
        else:
            return filename.rsplit(".")[0] +"."+ filetype

def create_csv_data(filepath, htmlarray):
    file = open(filepath,'w',newline='')
    writer1 = writer(file)
    writer1.writerows(htmlarray)
    file.close()


def create_db_data(filepath, htmlarray, fake_data=False):
    #connect to data base
    connect = sqlite3.connect(filepath)
    curcer = connect.cursor()
    if fake_data == False:
        variabls = str(tuple(f'data{i} TEXT' for i in range(htmlarray.shape[1]))).replace('\'','')
        curcer.execute("CREATE TABLE IF NOT EXISTS information " + variabls)
        
        inputs = str(tuple('?' for i in range(htmlarray.shape[1]))).replace('\'','')

        # when get table from html page ,it is not include header
        for data in htmlarray:
            insert_string = "INSERT INTO information VALUES "+ inputs
            curcer.execute(insert_string, data)

    else:
        curcer.execute("CREATE TABLE IF NOT EXISTS information (username TEXT, name TEXT, sex CHAR(1), address TEXT, mail TEXT, birthdate DATE)")
    #
    # ('?', '?', '?') delete single cote with replace
        inputs = str(tuple('?' for i in range(htmlarray.shape[1]))).replace('\'','')

        # ignor header with 1:
        for data in htmlarray[1:]:
            insert_string = "INSERT INTO information VALUES "+ inputs
            curcer.execute(insert_string, data)

    # save and close the data base
    connect.commit()
    connect.close()


def create_xlsx_data(filepath, htmlarray):
    #create excle file
    excleFile = openpyxl.Workbook()
    # shoose action sheet
    sheet = excleFile.active

    
    #data
    for i in range(len(htmlarray)):
        for j in range( len(htmlarray[0])):
            sheet.cell(row=i + 1, column=j + 1).value =  htmlarray[i][j]
        
    
    excleFile.save(filepath)

# make faker data
def faker_data(row):
    list_data = []
    list_data.append(["username", "name", "sex", "address", "mail", "birthdate"])
    fake = Faker(current_app.config['FAKER_CREATED_LANG'])

    for _ in range(row):
            information = fake.simple_profile()
            list_data.append(
                              [
                                information["username"], 
                                information["name"], 
                                information["sex"], 
                                information["address"], 
                                information["mail"], 
                                information["birthdate"]
                              ]
                            )
    array_data = np.array(list_data)
    return array_data


def create_html_data(filepath, htmlarray):
    table = tabulate(htmlarray[1:], htmlarray[0], tablefmt="html")
    file = open(filepath,'w')
    file.write(table)
    file.close()

def create_file(filepath, filetype, htmlarray, fake_data=False):
    if filetype == 'csv':
        create_csv_data(filepath, htmlarray)
        
    elif filetype == 'db':
        create_db_data(filepath, htmlarray, fake_data)

    elif filetype == 'xlsx':
        if htmlarray.shape[1] > 1048576:
            return "excle file can create 1048576 raw max."
        create_xlsx_data(filepath, htmlarray)
    elif filetype == 'html':
        create_html_data(filepath, htmlarray)


    else:
        return 'The extension is not supported. '
    