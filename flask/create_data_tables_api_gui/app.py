from flask import Flask, request, jsonify, send_file, send_from_directory, request, render_template
from werkzeug.utils import secure_filename
from helpers import *
import os
app = Flask(__name__)

# folder name (files save init)
DATA_FOLDER_NAME = 'data'
app.config['DATA_FOLDER_NAME'] = DATA_FOLDER_NAME

# default file name 
FILE_NAME_DEFAULT = 'test'
app.config['FILE_NAME_DEFAULT'] = FILE_NAME_DEFAULT

# language for faker data
FAKER_CREATED_LANG = 'en_US'
app.config['FAKER_CREATED_LANG'] = FAKER_CREATED_LANG


#home page
@app.route('/', methods=["POST", "GET"])
def home():
    if request.method  == "POST":
        return jsonify({"error":"You should choose one of the following paths: /createtable or /createtable/html"}), 404
    else:
        return render_template("index.html", PageName="Py Tables")
    
# to create faker data
@app.route('/createtable', methods=["POST", "GET"])
def createtable():
    if request.method == "POST":
        """  
        send a JSON file to this page containing : 
        - filename  file name (optional) 
        - row       rows number
        - type      file data type

        """
        
        
        """file name"""
        # is filename in JSON file
        try:
            filename = request.json['filename']
        except KeyError:
            filename = app.config['FILE_NAME_DEFAULT']
            
        # chake if the filename is empty or null
        if  filename == None or filename == "" or type(filename) != str:
            filename = app.config['FILE_NAME_DEFAULT']
            
        """row"""
            # is row number in JSON file
        try:
            row = request.json['row']
        except (ValueError,KeyError):
            return jsonify({"error":"no rows"}), 404
        
        # chake if the row is an integer or string integer
        if type(row) != int:   
            try:
                row = int(row)
            except (ValueError, TypeError):
                return jsonify({"error":"row should be an integer"}), 404
        else:
            # the row number must be greader than or equal 1
            if row < 1:
                return jsonify({"error":"row should be greater than or equal 1"}), 404
        
        """type"""
        # is file type number in JSON file   
        try:    
            filetype = request.json['type']
        except (KeyError, ValueError):
            return jsonify({"error":"no file type"}), 404
        
        # chack if file type is string and not null
        if type(filetype) != str:
            return jsonify({"error":"file type is not string"}), 404
        if type(filetype) == None:
            return jsonify({"error":"fileee type is not string"}), 404
        
        
        # chack if file name has extantion if not add and secure_filename
        filename = chacke_filename_extantion(filename, filetype)
        filename = secure_filename(filename)
            

        #filepath (to save files)
        filepath = str(os.path.join(app.config["DATA_FOLDER_NAME"], filename))

        # get faker data
        array_data = faker_data(row)

        # to return list data
        if filetype == 'list':
            return jsonify({"data":array_data.tolist()}), 201
        
        # create file (get file name and file type from JSON file to create)
        AnyArror = create_file(filepath, filetype, array_data, fake_data=True)
        
        # chack if there are not any error
        if AnyArror != None:
            return jsonify({"error": AnyArror}) , 404
        
        # return file value
        return send_from_directory(app.config['DATA_FOLDER_NAME'], filename)
    else:
        return render_template("createtable.html", PageName="create web table")
        



#create table from html table
@app.route('/createtable/html', methods=["POST", "GET"])
def createtable_html():
    if request.method == "POST":
        """
        send a JSON file to this page containing : 
        - filename  file name (optional)
        - weburl    URL
        - tablenum  table number in web page
        - type      file data type      
        """
        
        """filename"""
        # is file name in JSON file
        try:
            filename = request.json['filename']
        except KeyError:
            filename = app.config['FILE_NAME_DEFAULT']
        
        # chake the name is not empty or null
        if  filename == None or filename == "" or type(filename) != str:
            filename = app.config['FILE_NAME_DEFAULT']
        
        """weburl"""
        # is URL in JSON file
        try:
            weburl = request.json['weburl']
        except KeyError:
            return jsonify({"error":"no url sended"}), 404
        
        # chake the URL is not empty or null or number
        if  weburl == None or weburl == "" :
            return jsonify({"error":"url is not send"}), 404
        if  type(weburl) != str :
            return jsonify({"error":"url must be string"}), 404
        
        """tablenum"""
        # is table number in JSON file
        try:
            tablenum = int(request.json['tablenum'])
        except:
            return jsonify({"error":"table number is not corrcect"}), 404
        
        # chack table number is an integer or string integer
        if type(tablenum) != int:
            try:
                tablenum = int(tablenum)
            except:
                return jsonify({"error":"table number is not corrcect"}), 404
        if tablenum < 1:
                return jsonify({"error":"table number must be greater than or equal 1"}), 404
            
        """filetype""" 
        # is file type in json file 
        try:
            filetype = request.json['type']
        except:
            return jsonify({"error":"file type is not correct"}), 404
        
        # chack if it is string
        if type(filetype) != str:
            return jsonify({"error":"file type is not string"}), 404 
        
        # chacke the extantion and secure file name
        filename = chacke_filename_extantion(filename, filetype)
        filename = secure_filename(filename)
        
        #filepath
        filepath = str(os.path.join(app.config["DATA_FOLDER_NAME"], filename))
        
        #chack if URL is corrcect
        htmlarray = html_to_array(weburl, tablenum)
        if htmlarray != None:
            return jsonify({"error":"url not found"}),404
        
        # delete unicode character because it causes problems while writing in files
        htmlarray = delete_unicode(htmlarray)

        # to return list value
        if filetype == 'list':
            return jsonify({"data":htmlarray.tolist()}), 201


        
        # create file
        AnyArror = create_file(filepath, filetype, htmlarray)

        # chack if there are not any error
        if AnyArror != None:
            return jsonify({"error": AnyArror}) , 404
        
        # return file value
        return send_from_directory(app.config['DATA_FOLDER_NAME'], filename)
    else:
        return render_template("createWebTable.html",PageName="create web table")

@app.route('/createtableD/<string:way>', methods=["POST"])
def createtableD(way):
        """filename""" 
        try:
            filename = request.form['filename']
        except (KeyError, ValueError):
            filename = app.config['FILE_NAME_DEFAULT']
          
        if  filename == None or filename.strip() == "":
            filename = app.config['FILE_NAME_DEFAULT']
        """filetype"""
        try:
            filetype = request.form["type"]
        except (ValueError, KeyError):
            return "error :filename or row number in not correct"
        
        # chack if it is string
        if type(filetype) != str:
            return "error: file type is not string"
        #ملفات الفيكر الخاصة
        if str(way) == "faker":
            """row""" 
            try:
                row = int(request.form["row"])
            except (ValueError, KeyError):
                return "error :filename or row number in not correct"

            fake_data = True
            # get faker data
            array_data = faker_data(row)
        elif str(way) == "html": 
            #ملفات الويب الخاصة
            fake_data = False
            ##########################
            """weburl"""
            # is URL in JSON file
            try:
                weburl = request.form['weburl']
            except KeyError:
                return "error: no url sended"
            
            # chake the URL is not empty or null or number
            if  weburl == None or weburl == "" :
                return "error: url is not send"
            if  type(weburl) != str :
                return "error: url must be string"
            
            """tablenum"""
            # is table number in JSON file
            try:
                tablenum = request.form['tablenum']
            except:
                return "error: table number is not corrcect2"
            
            # chack table number is an integer or string integer
            if type(tablenum) != int:
                try:
                    tablenum = int(tablenum)
                except:
                    return "error: table number is not corrcect1"
            else:
                return "error: way is not correct"
            #chack if URL is corrcect
            htmlarray = html_to_array(weburl, tablenum)
            try:
                if htmlarray.startswith("error:"):
                    return  htmlarray
            except:
                pass
            # delete unicode character because it causes problems while writing in files
            htmlarray = delete_unicode(htmlarray)
            #########################
        
        # chacke the extantion and secure file name
        filename = chacke_filename_extantion(filename, filetype)
        filename = secure_filename(filename)
        
        #filepath (to save files)
        filepath = str(os.path.join(app.config["DATA_FOLDER_NAME"], filename))

        # create file
        AnyArror = create_file(filepath, filetype, array_data, fake_data)
        
        # chack if there are not any error
        if AnyArror != None:
            return "error: "+ AnyArror
        if filetype == 'csv':
            mimetype_value = 'application/csv'
        elif filetype == 'db':
            mimetype_value = "application/x-sqlite3"
        elif filetype == 'xlsx':
            mimetype_value = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        elif filetype == 'html':
            mimetype_value = 'text/html'
        else:
            return "error :extention is not support"

        return send_file(open(filepath,'rb'), mimetype = mimetype_value, as_attachment=True, download_name = filename)

@app.route('/createtableDhtml', methods=["POST"])
def createtableDhtml():
        """filename"""
        # is file name in JSON file
        # (
        try:
            filename = request.form['filename']
        except KeyError:
            filename = app.config['FILE_NAME_DEFAULT']
        # chake the name is not empty or null
        if  filename == None or filename == "" or type(filename) != str:
            filename = app.config['FILE_NAME_DEFAULT']
        # )
        """filetype""" 
        # is file type in json file 
        try:
            filetype = request.form['type']
        except:
            return jsonify({"error":"file type is not correct"}), 404
        
        # chack if it is string
        if type(filetype) != str:
            return jsonify({"error":"file type is not string"}), 404 
        ##########################
        """weburl"""
        # is URL in JSON file
        try:
            weburl = request.form['weburl']
        except KeyError:
            return "error: no url sended"
        
        # chake the URL is not empty or null or number
        if  weburl == None or weburl == "" :
            return "error: url is not send"
        if  type(weburl) != str :
            return "error: url must be string"
        
        """tablenum"""
        # is table number in JSON file
        try:
            tablenum = request.form['tablenum']
        except:
            return "error: table number is not corrcect2"
        
        # chack table number is an integer or string integer
        if type(tablenum) != int:
            try:
                tablenum = int(tablenum)
            except:
                return "error: table number is not corrcect1"
    
        #chack if URL is corrcect
        htmlarray = html_to_array(weburl, tablenum)
        try:
            if htmlarray.startswith("error:"):
                return  htmlarray
        except:
            pass
        # delete unicode character because it causes problems while writing in files
        htmlarray = delete_unicode(htmlarray)
        #########################
        
        # chacke the extantion and secure file name
        filename = chacke_filename_extantion(filename, filetype)
        filename = secure_filename(filename)
        
        #filepath
        filepath = str(os.path.join(app.config["DATA_FOLDER_NAME"], filename))
        
        # create file
        AnyArror = create_file(filepath, filetype, htmlarray)

        # chack if there are not any error
        if AnyArror != None:
            return jsonify({"error": AnyArror}) , 404
        
        if filetype == 'csv':
            mimetype_value = 'application/csv'
        elif filetype == 'db':
            mimetype_value = "application/x-sqlite3"
        elif filetype == 'xlsx':
            mimetype_value = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        elif filetype == 'html':
            mimetype_value = 'text/html'
        else:
            return "error :extention is not support"
              
        
         
        return send_file(open(filepath,'rb'), mimetype = mimetype_value, as_attachment=True, download_name = filename)



@app.before_request
def before():
    if not os.path.exists(DATA_FOLDER_NAME):
            os.mkdir(DATA_FOLDER_NAME)



#run the code
app.run(debug=True)