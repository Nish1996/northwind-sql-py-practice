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

Then we need to write up the SQL connector by importing 'pyodbc'