import pyodbc

# Variables to connect to the Database
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE=' +database+';UID='+username+';PWD='+password)

cursor = docker_Northwind.cursor()

all_null_fax = cursor.execute("SELECT ContactName, CompanyName, Phone FROM Customers WHERE Fax IS NULL;")

while True:
    row_record = all_null_fax.fetchone()
    if row_record is None:
        break
    print(row_record.ContactName, '--', row_record.CompanyName, '--', row_record.Phone)