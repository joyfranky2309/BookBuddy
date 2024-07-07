from django.contrib import admin
from django.urls import include, path
from LMS.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('addbook',addbook),
    path('uploadstatus',addbookdata),
    path('viewbooks',viewbook,name="view_books"),
    path('editbook/<str:title>/', edit_book, name='edit_book'),
    path('deletebook/<str:title>/', delete_book, name='delete_book'),
    path('issuebooks',borrow_book,name="issuebooks"),
    path('addstudent/', add_student, name='add_student'),
    path('editstudent/<str:roll_number>/', edit_student, name='edit_student'),
    path('viewstudents/', view_students, name='view_students'),
    path('accounts/', include('django.contrib.auth.urls')),
     path('logout/', logout_view, name='logout'),
]
