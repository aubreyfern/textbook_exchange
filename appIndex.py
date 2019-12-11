from flask import Flask, request, render_template, redirect, url_for
from wtforms import Form, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired
import pymysql
import datetime
import time
import config

app = Flask(__name__)

db = config.Database
db.__init__(db)

class Subjects:
    db = config.Database
    db.__init__(db)
    cur = db.__getitem__(db)
    con = db.__getstate__(db)

    def list_se(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 10 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_cs(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 5 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_biochem(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 1 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_fs(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 2 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_biology(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 3 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_chemistry(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 4 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_dataAnalytics(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 6 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_env(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 7 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_math(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 8 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result


    def list_physics(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId WHERE Books.SubjectId = 9 GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result

    def list_all(self):
        db.cur.execute(
            "SELECT Books.BookId, Books.BookName, Books.Isbn, Class.ClassName, Books.Required, Books.Quantity FROM Books INNER JOIN Transactions ON Books.BookId = Transactions.BookID INNER JOIN Class on Books.ClassId = Class.ClassId  GROUP BY Books.BookId")
        result = self.cur.fetchall()
        return result


class MusicSearchForm(Form):
    search = StringField('')


class searchForm(Form):
    choice = [('name','name'),
              ('Id','id')]
    select = SelectField('Search:', choices=choice)

@app.route('/software-engineering', methods=['GET','POST'])
def se():
    def db_query():
        db = Subjects()
        books = db.list_se()

        return books

    result = db_query()
    data='Software Engineering'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/computer-science', methods=['GET','POST'])
def cs():
    def db_query():
        db = Subjects()
        books = db.list_cs()

        return books

    result = db_query()
    data='Computer Science'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/biochemistry', methods=['GET','POST'])
def biochemistry():
    def db_query():
        db = Subjects()
        books = db.list_biochem()

        return books

    result = db_query()
    data='Biochemistry'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/food-science', methods=['GET','POST'])
def foodScience():
    def db_query():
        db = Subjects()
        books = db.list_fs()

        return books

    result = db_query()
    data='Food Science'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/biology', methods=['GET','POST'])
def biology():
    def db_query():
        db = Subjects()
        books = db.list_biology()

        return books

    result = db_query()
    data='Biology'
    return render_template('index.html', result=result, content_type='application/json',data=data)

@app.route('/chemistry', methods=['GET','POST'])
def chemistry():
    def db_query():
        db = Subjects()
        books = db.list_chemistry()

        return books

    result = db_query()
    data='Chemistry'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/data-analytics', methods=['GET','POST'])
def dataAnalytics():
    def db_query():
        db = Subjects()
        books = db.list_dataAnalytics()

        return books

    result = db_query()
    data='Data Analytics'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/environmental-science', methods=['GET','POST'])
def env():
    def db_query():
        db = Subjects()
        books = db.list_env()

        return books

    result = db_query()
    data='Environmental Science & Policy'
    return render_template('index.html', result=result, content_type='application/json',data=data)

@app.route('/math', methods=['GET','POST'])
def math():
    def db_query():
        db = Subjects()
        books = db.list_math()

        return books

    result = db_query()
    data = 'Math'
    return render_template('index.html', result=result, content_type='application/json',data=data)

@app.route('/physics', methods=['GET','POST'])
def physics():
    def db_query():
        db = Subjects()
        books = db.list_physics()

        return books

    result = db_query()
    data = 'Physics'
    return render_template('index.html', result=result, content_type='application/json',data=data)


@app.route('/donate',methods=['GET','POST'])
def donate():
    return render_template('donate.html', content_typ='application/json')


@app.route('/', methods=['GET','POST'])
def all():
    def db_query():
        db = Subjects()
        books = db.list_all()
        return books
    doAll='ud'
    result = db_query()
    data = 'All Books Available'
    return render_template('index.html', result=result, content_type='application/json', data = data, form=search,
                           doAll=doAll)

@app.route('/search', methods=['GET', 'POST'])
def search():
    db = Subjects()
    e = request.form['search']

    def db_query():
        if request.method == "POST":
            c=db.cur
          #  c.execute("SELECT DISTINCT BookName, Isbn, ClassName, Required, Quantity FROM Transactions t INNER JOIN Books b ON t.BookID = b.BookId INNER JOIN Class c ON b.ClassId = c.ClassId INNER JOIN Subjects s ON c.SubjectId = s.SubjectId WHERE Quantity>0 AND(BookName LIKE s% OR Subject LIKE s% OR ClassName LIKE s%) ORDER BY Quantity ASC", (request.form['search'], request.form['search'], request.form['search']))
            c.execute("SELECT DISTINCT BookName, Isbn, ClassName, Required, Quantity FROM Transactions t INNER JOIN Books b ON t.BookID = b.BookId INNER JOIN Class c ON b.ClassId = c.ClassId INNER JOIN Subjects s ON c.SubjectId = s.SubjectId WHERE Quantity>0 AND(BookName LIKE  %s OR Subject LIKE  %s OR ClassName LIKE %s) ORDER BY Quantity ASC", (('%'+request.form['search']+'%'), ('%'+request.form['search']+'%'), ('%'+request.form['search']+'%')))

            books = c.fetchall()
        return books
    result = db_query()
    data = request.form['search']
    return render_template('index.html', content_type='application/json',result=result,data=data)


@app.route('/export', methods=['GET','POST'])
def export():
    import cvsWriter
    def db_query():
        db = Subjects()
        books = db.list_all()


        return books

    result = db_query()
    data = 'All Books Available'
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')
    exported = 'Export successful! ' + st
    return render_template('index.html', result=result, content_type='application/json', data = data, exported=exported)


@app.route('/donate', methods=['GET','POST'])
def donateRedirect():
    return render_template('donate.html', content_type='application/json')



@app.route('/donateInput', methods=['GET','POST'])
def donateInput():
    db = Subjects()

    def db_query():
        if request.method == "POST":
            c = db.cur
            con = db.con
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["bookId"])
            if c.rowcount == 0:
                name = "This book cannot be found in the system. Donate an existing book or add a new textbook in the system."
                return name
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["stuId"])
            if c.rowcount == 0:
                name = "This student cannot be found in the system. Enter a valid student ID."
                return name
            else:
                c.execute("INSERT INTO Transactions(StudentId,BookID,TransactionType) VALUES (%s,%s, %s)", (request.form["stuId"], request.form["bookId"], 0))
                con.commit()
                c.execute("UPDATE Books SET Quantity = Quantity +1 WHERE BookId = %s", request.form["bookId"])
                con.commit()
                c.execute("SELECT BookName FROM Books WHERE BookId=%s",request.form["bookId"])
                result = c.fetchone()
                name = "You donated ",str(result.get('BookName'))
        return name
    data=db_query()
    return render_template('donate.html', content_type='application/json', data=data)

    db_query()
    return render_template('donate.html', content_type='application/json')

@app.route('/transactions',methods=['GET','POST'])
def transactionsRedirect():
    return render_template('transactions.html', content_type='application/json')


@app.route('/transactionsSearch',methods=['GET','POST'])
def transactionsSearch():
    db = Subjects()
    e = request.form['search']

    def db_query():
        if request.method == "POST":
            c = db.cur
            #  c.execute("SELECT DISTINCT BookName, Isbn, ClassName, Required, Quantity FROM Transactions t INNER JOIN Books b ON t.BookID = b.BookId INNER JOIN Class c ON b.ClassId = c.ClassId INNER JOIN Subjects s ON c.SubjectId = s.SubjectId WHERE Quantity>0 AND(BookName LIKE s% OR Subject LIKE s% OR ClassName LIKE s%) ORDER BY Quantity ASC", (request.form['search'], request.form['search'], request.form['search']))

            c.execute("SELECT DISTINCT * FROM Transactions INNER JOIN Books ON Transactions.BookID = Books.BookId INNER JOIN Subjects ON Books.SubjectId = Subjects.SubjectId WHERE Transactions.StudentId = %s ORDER BY Transactions.TransactionType ASC", request.form["search"])

            books = c.fetchall()
        return books


    def db_stu():
        if request.method=="POST":
            c = db.cur
            c.execute("SELECT DISTINCT * FROM Students WHERE StudentId= %s", request.form["search"])
           # c.execute("SELECT DISTINCT * FROM Transactions INNER JOIN Books ON Transactions.BookID = Books.BookId INNER JOIN Subjects ON Books.SubjectId = Subjects.SubjectId WHERE Transactions.StudentId = %s ORDER BY Transactions.TransactionType ASC", request.form["search"])
            student = c.fetchall()
        return student
    result = db_query()
    stu = db_stu()
    data = request.form['search']
    return render_template('transactions.html', content_type='application/json', result=result, stu=stu, data=data)


@app.route('/update',methods=['GET','POST'])
def updateSearch():
    db = Subjects()
    e = request.form['search']

    def db_query():
        if request.method == "POST":
            c = db.cur
            c.execute("SELECT DISTINCT * FROM Transactions INNER JOIN Books ON Transactions.BookID = Books.BookId INNER JOIN Subjects ON Books.SubjectId = Subjects.SubjectId WHERE Transactions.StudentId = %s ORDER BY Transactions.TransactionType ASC",request.form["search"])
            books = c.fetchall()
        return books

    db_query()
    return render_template('transactions.html', content_type='application/json')


@app.route('/delete',methods=['GET','POST'])
def deleteRedirect():
    return render_template('delete.html', content_type='application/json')


@app.route('/deleteSearch',methods=['GET','POST'])
def deleteSearch():
    db = Subjects()
    e = request.form['search']

    def db_query():
        if request.method == "POST":
            c = db.cur
            con = db.con
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["search"])
            result = c.rowcount
            if result == 0:
                name = "This book has either never existed in the system or has already been deleted from the system."
                return name
            else:
                res = c.fetchone()
                c.execute("DELETE FROM Transactions WHERE BookId = %s",request.form["search"])
                con.commit()
                c.execute("DELETE FROM Books WHERE BookId = %s",request.form["search"])
                con.commit()
                name = "You deleted ",str(res.get('BookName'))
                return name

    data = db_query()
    return render_template('delete.html', content_type='application/json', data=data)



@app.route('/checkOutRedirect',methods=['GET','POST'])
def checkOutRedirect():
    return render_template('checkOut.html', content_type='application/json')




@app.route('/checkOutInput', methods=['GET','POST'])
def checkOutInput():
    db = Subjects()

    def db_query():
        if request.method == "POST":
            c = db.cur
            con = db.con
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["bookId"])
            result = c.fetchone()
            if c.rowcount == 0:
                name = "This book cannot be found in the system. Find an available book."
            elif int(result.get('Quantity')) <= 0:
                name="This book is currently out of stock. Find a student to donate one!"
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["stuId"])
            result = c.fetchone()
            if c.rowcount == 0:
                name = "This student cannot be found in the system. Enter a valid student ID."
            else:
                c.execute("INSERT INTO Transactions(StudentId,BookID,TransactionType) VALUES (%s,%s, %s)", (request.form["stuId"], request.form["bookId"], 1))
                con.commit()
                c.execute("UPDATE Books SET Quantity = Quantity - 1 WHERE BookId = %s", request.form["bookId"])
                con.commit()
                c.execute("SELECT BookName FROM Books WHERE BookId=%s",request.form["bookId"])
                name = "You checked out ",str(result.get('BookName'))
        return name
    data=db_query()
    return render_template('checkOut.html', content_type='application/json', data=data)



@app.route('/UpdateInput', methods=['GET','POST'])
def addNeInput():
    db = Subjects()

    def db_query():
        if request.method == "POST":
            c = db.cur
            con = db.con
            c.execute("SELECT * FROM Books WHERE BookId = %s", request.form["bookId"])
            result = c.fetchone()
            if int(result.get('Quantity')) <= 0:
                name="This book is currently out of stock. Find a student to donate one!"
            else:
                c.execute("INSERT INTO Transactions(StudentId,BookID,TransactionType) VALUES (%s,%s, %s)", (request.form["stuId"], request.form["bookId"], 1))
                con.commit()
                c.execute("UPDATE Books SET Quantity = Quantity - 1 WHERE BookId = %s", request.form["bookId"])
                con.commit()
                c.execute("SELECT BookName FROM Books WHERE BookId=%s",request.form["bookId"])
                name = "You checked out ",str(result.get('BookName'))
        return name
    def subj_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT * FROM Subjects")
        subs= c.fetchall()
        return subs
    list2 = subj_qry()
    data=db_query()
    return render_template('addBook.html', content_type='application/json', data=data, dropdown_list = list2)


@app.route('/addNewInput',methods=['GET','POST'])
def addNewInput():
    db = Subjects()

    def subj_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT Subject FROM Subjects")
        subs= c.fetchall()
        return subs

    def class_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT ClassId FROM Class")
        cl = c.fetchall()
        return cl

    def req_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT DISTINCT Required FROM Books")
        reqs = c.fetchall()
        return reqs

    subs_list = subj_qry()
    class_list = class_qry()
    reqs_list = req_qry()

    def db_query():
        con = db.con
        c = db.cur
        c.execute(
            "INSERT INTO Books(BookId, BookName,Isbn,Quantity) VALUES (%s,%s,%s, %s)",
            (request.form["bookId"], request.form["bookName"], request.form["isbn"], 0))
        con.commit()
        name = str(request.form["bookName"]) , " was added to system."

        return name

    if request.method=="POST":
        data = db_query()


    return render_template('addBook.html', content_type='application/json', subs_list=subs_list, class_list = class_list,
                           req_list=reqs_list, data=data)


@app.route('/updateRedirect',methods=['GET','POST'])
def updateRedirect():
    def subj_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT Subject  FROM Subjects")
        subs= c.fetchall()
        return subs

    def class_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT ClassId FROM Class")
        cl = c.fetchall()
        return cl

    def req_qry():
        con = db.con
        c = db.cur
        c.execute("SELECT DISTINCT Required FROM Books")
        reqs = c.fetchall()
        return reqs

    subs_list = subj_qry()
    class_list = class_qry()
    reqs_list = req_qry()
    data='lkdf'
    return render_template('addBook.html', content_type='application/json', subs_list=subs_list, class_list = class_list,
                           req_list=reqs_list,data=data)
