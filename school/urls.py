from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_request, name="login"),
    path('home/', views.home, name="home"),
    path('logout', views.logout_request, name="logout"),
    #auth routes
    path('add_unit/', views.addUnit, name="addunit"),
    path('manage_units/', views.manageUnits, name="manageunits"),
    path('manage_units/edit_unit/<int:pk>', views.editUnit, name="editunit"),
    path('manage_units/delete_unit/<int:pk>', views.deleteUnit, name="deleteunit"),

    path('add_acadyear/', views.addAcadYear, name="addacadyear"),
    path('manage_acadyears/', views.manageAcadYears, name="manageacadyears"),
    path('manage_acadyears/edit_acadyear/<int:pk>', views.editAcadYear, name="editacadyear"),
    path('manage_acadyears/delete_acadyear/<int:pk>', views.deleteAcadYear, name="deleteacadyear"), 

    path('add_invoice/', views.addInvoice, name="addinvoice"),
    path('manage_invoices/', views.manageInvoices, name="manageinvoices"),
    path('manage_invoices/edit_invoice/<int:pk>', views.editInvoice, name="editinvoice"),
    path('manage_invoices/delete_invoice/<int:pk>', views.deleteInvoice, name="deleteinvoice"), 

    path('add_staff/', views.addStaff, name="addstaff"),
    path('manage_staff/', views.manageStaff, name="managestaff"),
    path('manage_staff/edit_staff/<int:pk>', views.editStaff, name="editstaff"),
    path('manage_staff/delete_staff/<int:pk>', views.deleteStaff, name="deletestaff"),  

    path('add_student/', views.addStudent, name="addstudent"),
    path('manage_students/', views.manageStudents, name="managestudents"),
    path('manage_students/edit_student/<int:pk>', views.editStudent, name="editstudent"),
    path('manage_students/delete_student/<int:pk>', views.deleteStudent, name="deletestudent"),       

]