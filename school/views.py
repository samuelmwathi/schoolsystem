from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import *

# Create your views here.
def index(request):
    return render(request, 'school/index.html')

def login_request(request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

        form = AuthenticationForm()
        return render(request, 'school/login.html', context={ 'form': form })  

def home(request):
    return render(request, 'school/home.html')   

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")

def addUnit(request):
    form = UnitForm
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Details saved successfully")
            return redirect('addunit')
    return render(request, 'auth/units/add_unit.html', {'form':form})

def manageUnits(request):
    units = Unit.objects.all()
    return render(request, 'auth/units/manage_units.html', {'units':units})   

def editUnit(request, pk):
    unit = Unit.objects.filter(pk=pk)
    return render(request, 'auth/units/edit_unit.html', {'unit':unit})

def deleteUnit(request, pk):
    unit = Unit.objects.filter(pk=pk)
    return render(request, 'auth/units/delete_unit.html', {'unit':unit}) 

def addAcadYear(request):
    form = AcadYearForm
    if request.method == 'POST':
        form = AcadYearForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Details saved successfully")
            return redirect('addacadyear')
    return render(request, 'auth/acadyears/add_acadyear.html', {'form':form})

def manageAcadYears(request):
    acadyears = AcadYear.objects.all()
    return render(request, 'auth/acadyears/manage_acadyears.html', {'acadyears':acadyears})   

def editAcadYear(request, pk):
    acadyear = AcadYear.objects.filter(pk=pk)
    return render(request, 'auth/acadyears/edit_acadyear.html', {'acadyear':acadyear})

def deleteAcadYear(request, pk):
    acadyear = AcadYear.objects.filter(pk=pk)
    return render(request, 'auth/acadyears/delete_acadyear.html', {'acadyear':acadyear})

# invoice
def addInvoice(request):
    form = InvoiceForm
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Details saved successfully")
            return redirect('addinvoice')
    return render(request, 'auth/invoices/add_invoice.html', {'form':form})

def manageInvoices(request):
    invoices = Invoice.objects.all()
    return render(request, 'auth/invoices/manage_invoices.html', {'invoices':invoices})   

def editInvoice(request, pk):
    invoice = Invoice.objects.filter(pk=pk)
    return render(request, 'auth/invoices/edit_invoice.html', {'invoice':invoice})

def deleteInvoice(request, pk):
    invoice = Invoice.objects.filter(pk=pk)
    return render(request, 'auth/invoices/delete_invoice.html', {'invoice':invoice})    

# staff
def addStaff(request):
    form = StaffRegistrationForm
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Details saved successfully")
            return redirect('addstaff')
    return render(request, 'auth/staff/add_staff.html', {'form':form})

def manageStaff(request):
    users = User.objects.filter(is_staff=True)
    return render(request, 'auth/staff/manage_staff.html', {'users':users})   

def editStaff(request, pk):
    user = User.objects.filter(pk=pk)
    return render(request, 'auth/staff/edit_staff.html', {'user':user})

def deleteStaff(request, pk):
    user = User.objects.filter(pk=pk)
    return render(request, 'auth/staff/delete_staff.html', {'user':user})   

# student
def addStudent(request):
    form = StudentRegistrationForm
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Details saved successfully")
            return redirect('addstudent')
    return render(request, 'auth/students/add_student.html', {'form':form})

def manageStudents(request):
    users = User.objects.filter(is_staff=True)
    return render(request, 'auth/students/manage_students.html', {'users':users})   

def editStudent(request, pk):
    user = User.objects.filter(pk=pk)
    return render(request, 'auth/students/edit_student.html', {'user':user})

def deleteStudent(request, pk):
    user = User.objects.filter(pk=pk)
    return render(request, 'auth/students/delete_student.html', {'user':user})         

