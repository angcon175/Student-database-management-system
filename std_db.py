import sqlite3

def studentData():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text,FirstName Text,LastName text,DoB text,Age text,gender text,Address text,Mobile text)")
	con.commit()
	con.close()
	
def addStdRec(StdID, FirstName,LastName,DoB,Age,Gender,Address,Mobile):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?)",(StdID,FirstName,LastName,DoB,Age,Gender,Address,Mobile))
	con.commit()
	con.close()
	
def viewData():
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM student")
	rows=cur.fetchall()
	con.close()
	return rows

def deleteRec(id):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("DELETE FROM student WHERE id=?",(id,))
	con.commit()
	con.close()
	
def searchData(StdID="",FirstName="",LastName="",DoB="",Age="",Gender="",Address="",Mobile=""):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("SELECT * FROM student WHERE StdID=? OR FirstName=? OR LastName=? OR DoB=? OR Age=? OR Gender=? OR Address=? OR Mobile=?",(StdID,FirstName,LastName,DoB,Age,Gender,Address,Mobile))
	rows=cur.fetchall()
	con.close()
	return rows
	
def dataUpdate(id,StdID="",FirstName="",LastName="",DoB="",Age="",Gender="",Address="",Mobile=""):
	con=sqlite3.connect("student.db")
	cur=con.cursor()
	cur.execute("UPDATE student SET StdID=?,FirstName=?,LastName=?,DoB=?,Age=?,Gender=?,Address=?,Mobile=?,WHERE id=?",(StdID,FirstName,LastName,DoB,Age,Gender,Address,Mobile,id))
	con.commit
	con.close()

studentData()
