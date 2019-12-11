import csv
import pymysql

try:
   host = "104.199.117.142"
   user = "abby"
   password = "cpsc408"
   db = "cpsc408"

   con = pymysql.connect(host=host, user=user, password=password, db=db,
                                  cursorclass=pymysql.cursors.DictCursor)

   query = "SELECT * FROM Books INNER JOIN Subjects ON Books.SubjectId = Subjects.SubjectId WHERE Books.Quantity > 0 ORDER BY Books.SubjectId"
   cursor = con.cursor()
   cursor.execute(query)
   records = cursor.fetchall()
   print("AVAILABLE ROOMS", cursor.rowcount)
   cursor.close()
   csvData= [['AVAILABLE BOOKS', '','','','','',''],
             ['Book ID', 'BookName', 'ISBN', 'Subject', 'Class', 'Required', 'Quantity']]

   for row in records:
       dataRow = str(row.get('BookId'))
       id = str(row.get('BookId'))
       name = str(row.get('BookName'))
       isbn = str(row.get('Isbn'))
       subject = str(row.get('Subject'))
       classNum = str(row.get('ClassId'))
       yes = row.get('Required')
       if yes == 1:
        required = 'Yes'
       else:
        required = 'No'
       quant = str(row.get('Quantity'))
       csvData.append([id, name, isbn, subject, classNum, required, quant])

   with open('Books.csv','w') as csvFile:
       for d in csvData:
        csv.writer(csvFile).writerow(d);
       print("wrote to file - available")
   csvFile.close()

   noQuery = "SELECT * FROM Books INNER JOIN Subjects ON Books.SubjectId = Subjects.SubjectId WHERE Books.Quantity = 0 ORDER BY Books.SubjectId"
   cursor = con.cursor()
   cursor.execute(noQuery)
   noRecords = cursor.fetchall()
   print("\nUNAVAILABLE ROWS: ", cursor.rowcount)
   cursor.close()
   noCsvData= [['', '','','','','',''],['UNAVAILABLE BOOKS', '','','','','',''],['Book ID', 'BookName', 'ISBN', 'Subject', 'Class', 'Required', 'Quantity']]

   for row in noRecords:
       dataRow = row.get('BookId')
       id = row.get('BookId')
       name = row.get('BookName')
       isbn = row.get('Isbn')
       subject = row.get('Subject')
       classNum = row.get('ClassId')
       yes = row.get('Required')
       if yes == 1:
        required = 'Yes'
       else:
        required = 'No'
       quant = row.get('Quantity')
       noCsvData.append([id, name, isbn, subject, classNum, required, quant])

   with open('Books.csv','a') as csvFile:
       writer = csv.writer(csvFile, delimiter=',')
       for d in noCsvData:
           writer.writerow(d)
       print("wrote to file - unavailable")
   csvFile.close()

except Exception as e:
    print (e)