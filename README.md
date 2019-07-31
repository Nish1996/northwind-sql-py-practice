#SQL to Python Linkages - Homework Exercise

##Requirements
This exercise is to help further consolidate the linkages and connections between Python and SQL and vice-versa

What is needed:
1) Make cursor with SQL query and the SQL query should filter WHERE fax is Null
2) Fetchall from cursor
3) Iterate over the cursor and get out the relevant information
4) We need their company name, contact name and phone number

##Solution to Problem
First of all we need to install 'pyodbc' from the Settings panel:
````
File -- Settings -- Project -- 
Project Interpreter -- + -- 
Search for 'pyodbc' -- Install
````

Then we need to write up the SQL connector by importing 'pyodbc' and establishing the connection:
````
import pyodbc

# Variables to connect to the Database
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_Northwind = pyodbc.connect(
'DRIVER={ODBC Driver 17 for SQL Server};
SERVER='+server+';DATABASE=' +database+';
UID='+username+';PWD='+password)
````

After we need to configure the cursor through SQL queries and return customers WHERE Fax IS NULL:

````
cursor = docker_Northwind.cursor()

all_null_fax = cursor.execute("SELECT ContactName, 
CompanyName, Phone FROM Customers WHERE Fax IS NULL;")
````

Then we need to establish a loop where Python will continue to retrieve all customers where their Fax number is not given by iterating over the existing cursor and retrieving company name, contact name and phone number:

````
while True:
    row_record = all_null_fax.fetchone()
    if row_record is None:
        break
    print(row_record.ContactName, '--', row_record.CompanyName, 
    '--', row_record.Phone)
    
    I have included delimiter style seperators to seperate the 
    three parts for each customer:
    
    Antonio Moreno -- Antonio Moreno Taquería -- (5) 555-3932
    Victoria Ashworth -- B's Beverages -- (171) 555-1212
    Yang Wang -- Chop-suey Chinese -- 0452-076545
    Pedro Afonso -- Comércio Mineiro -- (11) 555-7647
    Aria Cruz -- Familia Arquibaldo -- (11) 555-9857
    Maria Larsson -- Folk och fä HB -- 0695-34 67 21
    José Pedro Freyre -- Godos Cocina Típica -- (95) 555 82 82
    André Fonseca -- Gourmet Lanchonetes -- (11) 555-9482
    Howard Snyder -- Great Lakes Food Market -- (503) 555-7555
    Helen Bennett -- Island Trading -- (198) 555-8888
    Philip Cramer -- Königlich Essen -- 0555-09876
    Jaime Yorres -- Let's Stop N Shop -- (415) 555-5938
    Alexander Feuer -- Morgenstern Gesundkost -- 0342-023176
    Isabel de Castro -- Princesa Isabel Vinhos -- (1) 356-5634
    Lúcia Carvalho -- Queen Cozinha -- (11) 555-1189
    Horst Kloss -- QUICK-Stop -- 0372-035188
    Janete Limeira -- Ricardo Adocicados -- (21) 555-3412
    Michael Holz -- Richter Supermarkt -- 0897-034214
    Jose Pavarotti -- Save-a-lot Markets -- (208) 555-8097
    Liz Nixon -- The Big Cheese -- (503) 555-3612
    Miguel Angel Paolino -- Tortuga Restaurante -- (5) 555-2933
    Paula Parente -- Wellington Importadora -- (14) 555-8122
````

Finally we have to Git Bash all the processes and send to Github:

##*What is Git Bash?*
Git Bash is an application for Microsoft Windows environments which provides an emulation layer for a Git command line experience. Bash is an acronym for Bourne Again Shell. A shell is a terminal application used to interface with an operating system through written commands.

##*Line Commands in Git Bash for Customers Fax Query*
- Step 1 - Know the drivepoint access which you have
-      $ pwd -->
       /c/Users/AHirani
- Step 2 - List all directories in that drive (note that 'ls -a' will display the PyCharm queries for Naan Factory 2)
-      $ ls -a
- Step 3 - Access PyCharmProjects and the corresponding file and initialise an empty Git Repository
-      $ cd PycharmProjects
       $ git init
- Step 4 - Check Git Status
-      $ git status
- Step 5 - Add and commit the PyCharm processes for sql-to-py-prac
-      Since changes aren't committed:
       $ cd sql-to-py-prac.py
       $ git add .
       Then commit first save:
       $ git commit -m "Initialised repo"
       $ git add .
       Then commit second save:
       $ git commit -m "Completed all tasks and saved"
- Step 6 - Let Git create the changes in files and insert new data into the Repository
- Step 7 - Confirm Git Status after letting Git add into the repository
-      $ git status
       You will see this message:
       'On branch master nothing to commit, 
       working tree clean'

And there you have it. You have successfully completed the task and are on your way to understanding Python and SQL connections as well as having a further understanding of how to use Python and SQL Server in tandem to create excellent and amazing data outputs!
       
Please note: **the README.md (this file) needs to also be committed**

- Step 8: Add and commit the README.md file
-       $ git add README.md
        $ git commit -m "README.md compiled and completed
        $ git add README.md
        $ git commit -m "Added README.md in commit under Git
