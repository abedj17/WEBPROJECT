import _sqlite3
import sqlite3
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin

# Create your views here.
# def login(request):
#     return redirect(request,'STEP/register')
# return render(request,'STEP/login.html')
global user
user = ()

# ******************************************************************
# from django.shortcuts import render, redirect
# #from STEP.STEPAPP.forms import TeacherForm
#from STEP.STEPAPP.models import Teacher




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("error")

    return conn


def loginView(request):
    if request.method == 'POST':
        a = request.POST['select1']
        username1 = request.POST['username']
        password1 = request.POST['password']
        conn = create_connection("mydb.db")
        cur = conn.cursor()
        if a == '2':
            cur.execute("SELECT * FROM TeacherDetails")
        if a == '3':
            cur.execute("SELECT * FROM StudentDetails")
        if a == '4':
            cur.execute("SELECT * FROM AdminDetails")
        data = cur.fetchall()
        found = False
        #data2 = (dict(data))
        conn.close()
        print(username1,password1)
        print("----------")
        print(data)
        if a=='2' or a=='3':
            for i in data:
                if username1 in i and str(int(password1)) in i:
                    user = i
                    found = True
        else:
            data2 = (dict(data))
            if data2[str(password1)]==str(username1):
                found=True
        if found and a == '3':
            return redirect('StudentView')
        elif found and a == '2':
            return render(request, 'STEPAPP/profile.html', {"name": user[2], "lname": user[3]})
        elif found and a == '4':
            return render(request, 'STEPAPP/nevbaradmin.html')
        else:
            messages.error(request, 'Wrong username or password', extra_tags='safe')
            return render(request, 'STEPAPP/login.html')
       # # if username1 in data2.keys() and password1 == str(int(data2[username1])):
       #      if username1 in i and str(int(password1)) in i:
       #          user = i
       #          found = True
       #  if found and a == '3':
       #      return redirect('StudentView')
       #  if found and a =='2':
       #      return redirect('TeacherView')
       #  if found and a=='4':
       #      return redirect('TeacherView','StudentView')
       #  else:
       #      messages.error(request, 'Wrong username or password', extra_tags='safe')
       #      return render(request, 'STEPAPP/login.html')
    else:
        return render(request, 'STEPAPP/login.html')

def adminView(request):
    return render(request, 'STEPAPP/nevbaradmin.html')
def registerView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        firstname1 = request.POST['firstname']
        lastname1 = request.POST['lastname']
        email1 = request.POST['email']
        id1 = request.POST['id']
        subject1 = request.POST['subject']
        phonenumber1 = request.POST['phonenumber']
        a = request.POST['select1']
        '''if a == '2':
            cur.execute("SELECT username, password FROM TeacherDetails")
        if a == '3':
            cur.execute("SELECT username, password FROM StudentDetails")
        data = cur.fetchall()
        found = False
        data2 = (dict(data))
        cur = conn.cursor()'''
        print(password1)
        print("INSERT INTO TeacherDetails VALUES( " +"'" + password1 +"'" + " , " + "'" + username1 + "'" + " , " + "'" + firstname1 + "'" + " , " + "'" + lastname1 + "'" + " , " + "'" + email1 + "'" + " , " +"'" + id1 +"'" + " , " + "'" + subject1 + "'" + " , " +"'" + phonenumber1 +"'" + " )")
        if a == '2':
            cur.execute(
                "INSERT INTO TeacherDetails VALUES( " +"'" + password1 +"'" + " , " + "'" + username1 + "'" + " , " + "'" + firstname1 + "'" + " , " + "'" + lastname1 + "'" + " , " + "'" + email1 + "'" + " , " +"'" + id1 +"'" + " , " + "'" + subject1 + "'" + " , " +"'" + phonenumber1 +"'" + " )")
            conn.commit()
        if a == '3':
            cur.execute(
                "INSERT INTO StudentDetails VALUES( " +"'" + password1 +"'" + " , " + "'" + username1 + "'" + " , " + "'" + firstname1 + "'" + " , " + "'" + lastname1 + "'" + " , " + "'" + email1 + "'" + " , " +"'" + id1 +"'" + " , " + "'" + subject1 + "'" + " , " +"'" + phonenumber1 +"'" + " )")
            conn.commit()
    conn.close()
    return render(request, 'STEPAPP/register.html')


def profileVeiw(request):
    if user != '':
        return render(request, 'STEPAPP/home.html')


def StudentView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TeacherDetails")
    Teachers = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileStudent.html", {'Teachers': Teachers})

def TeacherView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentDetails")
    Students = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profile.html", {'Students': Students})

def logoutUser(request):
	return redirect('home-page')

'''def adminview(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentDetails")
    Students = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileTeacher.html", {'Students': Students})
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TeacherDetails")
    Teachers = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileStudent.html", {'Teachers': Teachers})'''
