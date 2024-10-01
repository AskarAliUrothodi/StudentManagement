from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from poll.models import Person
from poll.models import Students
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as loginpa
from django.utils.datastructures import MultiValueDictKeyError



# def home(request):
    # t=loader.get_template("home.html")
    # context={
    #     'name':'john',
    #     'age':21
    # }

    # return HttpResponse(t.render(context,request))

def deletestudent(request,id):
    t=loader.get_template("featured_listings.html")
    S=Students.objects.get(id=id)
    S.delete()
    return redirect('/featured_listings/')

@csrf_exempt
def updateprocess(request,id):
    t=loader.get_template("featured_listings.html")
    if request.method=="POST":
        student_name=request.POST["student_name"]
        admission_no=request.POST["admission_no"]
        dob=request.POST["dob"]
        address=request.POST["address"]
        phone=request.POST["phone"]
        
        S=Students.objects.get(id=id)
        
        S.student_name=student_name
        S.admission_no=admission_no
        S.dob=dob
        S.address=address
        S.phone=phone
    S.save()
    return redirect('/featured_listings/')
    


def updatestudent(request,id):
    t=loader.get_template("updatestudent.html")
    S=Students.objects.get(id=id)
    context={
        'S':S
    }
    return HttpResponse(t.render(context,request))

@csrf_exempt
def studentaddedsuccessful(request):
    t=loader.get_template("studentaddedsuccessful.html")
    return HttpResponse(t.render())



@csrf_exempt
def addstudentprocess(request):
    t=loader.get_template('studentaddedsuccessful.html')
    if request.method=="POST":
        student_name=request.POST['student_name']
        admission_no=request.POST['admission_no']
        dob=request.POST['dob']
        address=request.POST['address']
        phone=request.POST['phone']
        S=Students(student_name=student_name,admission_no=admission_no,dob=dob,address=address,phone=phone)
        S.save()
    return HttpResponse(t.render())


def featured_listings(request):
    t=loader.get_template("featured_listings.html")
    S=Students.objects.all()
    context={
        'S':S
    }
    return HttpResponse(t.render(context,request))

@csrf_exempt
def addpersonpageprocess(request):
    t=loader.get_template('addsuccess.html')
    if request.method=="POST":
        name=request.POST['name']
        eid=request.POST['eid']
        address=request.POST['address']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']
        p=Person(name=name,eid=eid,address=address,dob=dob,email=email,mob=mob)
        p.save()
    return HttpResponse(t.render())       



def addstudent(request):
    t=loader.get_template("addstudent.html")
    return HttpResponse(t.render())

def login1(request):
    t=loader.get_template("login1.html")
    return HttpResponse(t.render())


def new(request):
    t=loader.get_template("new.html")
    S=Students.objects.all()
    context={
        'S':S
    }
    return HttpResponse(t.render(context,request))




def loginp(request):
    t=loader.get_template("login.html")
    return HttpResponse(t.render())



def home(request):
    return render(request,'home.html',{
        'name':'john',
        'age': 21
    })


def Persons(request):
    t=loader.get_template("Persons.html")
    p=Person.objects.all()
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

def persondetails(request,id):
    t=loader.get_template("persondetails.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

def addperson(request):
    t=loader.get_template("addperson.html")
    return HttpResponse(t.render())

@csrf_exempt
def addpersonpageprocess(request):
    t=loader.get_template('addsuccess.html')
    if request.method=="POST":
        name=request.POST['name']
        eid=request.POST['eid']
        address=request.POST['address']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']
        p=Person(name=name,eid=eid,address=address,dob=dob,email=email,mob=mob)
        p.save()
    return HttpResponse(t.render())

def deleteperson(request,id):
    t=loader.get_template("deletedsuccess.html")
    p=Person.objects.get(id=id)
    p.delete()
    return HttpResponse(t.render())

def updateperson(request,id):
    t=loader.get_template("updatepage.html")
    p=Person.objects.get(id=id)
    context={
        'p':p
    }
    return HttpResponse(t.render(context,request))

@csrf_exempt
def updatepersonprocess(request,id):
    t=loader.get_template('updatesuccess.html')
    if request.method=="POST":
        name=request.POST['name']
        eid=request.POST['eid']
        address=request.POST['address']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']

        p=Person.objects.get(id=id)

        p.name=name
        p.address=address
        p.eid=eid
        p.email=email
        p.dob=dob
        p.mob=mob

    p.save()
    return HttpResponse(t.render())



def login(request):
    t=loader.get_template("login.html")
    context={
        'p':""
    }
    return HttpResponse(t.render(context,request))

def signup(request):
    t=loader.get_template("createaccount.html")
    return HttpResponse(t.render())

@csrf_exempt
def signpage(request):
    if request.method=='POST':
        name=request.POST["name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1!=password2:
            return HttpResponse("Password Entered is not match, please try again")
        else:
            user=User.objects.create_superuser(name,email,password1)
            print(user)
            user.save()
        return redirect("loginpage")
    

@csrf_exempt
def authenticating(request):
    if request.method=="POST":
        name=request.POST["name"]
        password1=request.POST["password1"]
        user=authenticate(username=name,password=password1)
        #user = authenticate(username="john", password="secret")
        if user:
            loginpa(request,user)
            return redirect("homepage")
