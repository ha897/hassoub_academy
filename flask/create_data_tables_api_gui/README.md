# flask web api
#### Video Demo:  <https://youtu.be/CU4pzQZG5-Q>
#### Description:
This project creates tables, either fake tables or tables extracted from web pages. It consists of two parts: an API that can be used for other applications by sending a JSON file to the project containing the file name, number of rows, and data type desired for output if fake tables are desired. If tables are to be extracted from a web page, the JSON file should contain the file name, URL, table order, and desired data type. The other part is a GUI where the user interacts to achieve the aforementioned purposes.

The project works by converting arrays with the NumPy library and then converting them to a table.

### Libraries used in the project:
- faker: to create web app
- NumPy: to create arrays
- Pandas: to create tables
- os: To handle paths.
- sqlite3: To handle database (When creating databases)
- openpyxl: To handle excel files
- tabulate: To create html tables

### The project consists of two parts:

#### API (When sending POST requests):
Users can interact with the application through other applications. There are two paths:
1. """/createtable"""
    - This project creates fake data in the following formats: csv, database, excel.
    - You can select the language of the created data by changing `FAKER_CREATED_LANG` to the language code you want. You can find a list of languages in the Faker library documentation: [Faker Documentation](https://faker.readthedocs.io/en/master/locales.html)
    - We send it (in JSON format):
        - filename (if there is no file name, it will use the default name specified in the settings)
        - row number of rows
        - type type of created table 
            - csv: CSV file
            - db: SQLite database
            - xlsx: Excel
            - list 
            - html
    - It creates a file containing a table with the following columns:
        - username
        - name
        - sex
        - address
        - mail
        - birthdate

2. """/createtable/html"""
    - This extracts a table from an HTML page and saves it as a table in the following data types: csv, database, excel.
    - We send it:
        - weburl: web page link
        - filename: file name (optional)
        - tablenum: table number (order on the HTML page)
        - type: type of table
            - csv: CSV file
            - db: SQLite database
            - xlsx: Excel
            - list: List type
    - It creates a file with the table 

#### GUI (When sending GIT requests):
User can interact with it directly. There are three paths:
1. """home"""
    - This is the main page of the application. Other paths can be selected from this page.
2. """createtable"""
    - This is the page where the user can create a faker table.
3. """createtable/html"""
    - This is the page where the user can create a table from web page.

### "Important Notes":
- Use POST format for API
- Use GIT format for GUI
- If the user doesn't submit a file name it will be the default name in Environment variables 
- If the user doesn't submit a folder name it will be the default name in Environment variables 
- If the user doesn't submit a faker language it will be the default name in Environment variables 
- This API works on port 8000 and the frontend on port 5000
- File name must not include "."
