import _sqlite3
import sqlite3
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin

# Create your views here.
global user
user = ()
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
    print(1)
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
        conn.close()
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
            return render(request, 'STEPAPP/profile.html', {"name": user[2], "lname": user[3],"subject":user[6],"username":user[1],"email":user[4],"phone":user[7],"id":5})
        elif found and a == '2':
            return render(request, 'STEPAPP/profile.html', {"name": user[2], "lname": user[3],"subject":user[6],"username":user[1],"email":user[4],"phone":user[7],"id":5})
        elif found and a == '4':
            return redirect('adminView')
        else:
            messages.error(request, 'Wrong username or password', extra_tags='safe')
            return render(request, 'STEPAPP/login.html')
    else:
        return render(request, 'STEPAPP/login.html')


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
    return render(request, "STEPAPP/profile.html",{'Teachers': Teachers})

def Students(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM TeacherDetails")
    Teachers = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileStudent.html",{'Teachers': Teachers})

def TeacherView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentDetails")
    Students = cur.fetchall()
    conn.close()
    a=('Teacher')
    return render(request, "STEPAPP/profile.html", {'Students': Students,'name':a})

def Teachers(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM StudentDetails")
    Students = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileTeacher.html", {'Students': Students})

def logoutUser(request):
    return redirect('home-page')


def profile(request):
    return redirect('TeacherView')


def adminView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    a = cur.execute("SELECT * FROM StudentDetails")
    Students = a.fetchall()
    b = cur.execute("SELECT * FROM TeacherDetails")
    teachers = b.fetchall()
    conn.close()
    return render(request, "STEPAPP/profileAdmin.html", {'Students': Students,'teachers': teachers})

def deleteStudent(request,id):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    a = cur.execute("SELECT * FROM StudentDetails")
    Students = a.fetchall()
    if request.method=='POST':
        delete = ("DELETE FROM StudentDetails WHERE id=?")
        cur.execute(delete, (str(id),))
        conn.commit()
        return redirect('adminView')
    context={'Students':Students}
    return render(request, "STEPAPP/delete.html", context)



def deleteTeacher(request,id):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    b = cur.execute("SELECT * FROM TeacherDetails")
    teachers = b.fetchall()
    if request.method=='POST':
        delete = ("DELETE FROM TeacherDetails WHERE id=?")
        cur.execute(delete, (str(id),))
        conn.commit()
        return redirect('adminView')
    context={'teachers':teachers}
    return render(request, "STEPAPP/deleteTeacher.html", context)

def updateStudent(request,id):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    b = cur.execute("select * from StudentDetails where StudentDetails.id = "+id)
    st = b.fetchall()
    if request.method == 'POST':
        update = """UPDATE StudentDetails SET firstname = ?, lastname=?, subject=?, phonenumber=? """
        cur = conn.cursor()
        cur.execute(update, str(id))
        conn.commit()
        cur.close()

    return render(request, "STEPAPP/updateStudent.html", {'Students': b})


def meeting(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    if request.method == 'POST':
        studentname1 = request.POST['studentname']
        teachername1 = request.POST['teachername']
        subject1 = request.POST['subject']
        date1 = request.POST['date']
        studentnumber1 = request.POST['studentnumber']

        cur.execute("INSERT INTO MeetingDetails VALUES( " + "'" + studentname1 + "'" + " , " + "'" + teachername1 + "'" + " , " + "'" + subject1 + "'" + " , " + "'" + date1 + "'" + " , " + "'" + studentnumber1 + "'" + " )")
        conn.commit()
    conn.close()
    return render(request, 'STEPAPP/meeting.html')

def meetingView(request):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM MeetingDetails")
    Meetings = cur.fetchall()
    conn.close()
    return render(request, "STEPAPP/meetingView.html", {'Meetings': Meetings})

def deleteMeeting(request,studentnumber):
    conn = create_connection("mydb.db")
    cur = conn.cursor()
    b = cur.execute("SELECT * FROM MeetingDetails")
    meetings = b.fetchall()
    if request.method=='POST':
        delete = ("DELETE FROM MeetingDetails WHERE studentnumber=?")
        cur.execute(delete, (str(studentnumber),))
        conn.commit()
        return redirect('meetingView')
    context={'meetings':meetings}

    return render(request, "STEPAPP/deletemeeting.html", context)
