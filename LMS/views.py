from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Student
from django.shortcuts import *
from django.http import HttpResponse
from .models import *
from .forms import BookForm 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout
# Create your views here.
@login_required
def home(request):
    return render(request,"Home.html")
@login_required
def addbook(request):
    return render(request,"addbook.html")
@login_required
def viewbook(request):
    books = Book.objects.all()
    return render(request,"viewbook.html",context={"books":books})
@login_required
def addbookdata(request):
     if request.method=="POST":
        title=request.POST["title"]
        author=request.POST["author"]
        isbn=request.POST["ISBN"]
        price=request.POST["price"]
        print(title,author,isbn,price)
        book=Book()
        book.title=title
        book.author=author
        book.isbn=isbn
        book.price=price
        book.save()
        return render(request,"uploadstatus.html",context={"status":"success"})
     else:
         return render(request,"uploadstatus.html",ccontext={"status":"failure"})

@login_required
def edit_book(request, title):
    book = get_object_or_404(Book, title=title)
    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.isbn = request.POST["isbn"]
        book.price = request.POST["price"]
        
        borrowed_by_ids = request.POST.getlist("borrowed_by")
        borrowed_by_students = Student.objects.filter(id__in=borrowed_by_ids)
        book.borrowed_by.set(borrowed_by_students)
        
        book.save()
        return redirect('view_books')
    
    all_students = Student.objects.all()
    return render(request, 'editbook.html', {'book': book, 'students': all_students})

def delete_book(request, title):
    book = get_object_or_404(Book, title=title)
    if request.method == "POST":
        book.delete()
        return redirect('view_books')
    return render(request, 'deletebook.html', {'book': book})
def borrow_book(request):
    if request.method == "POST":
        title = request.POST["title"]
        roll_number = request.POST["roll_number"]
        book = Book.objects.get(title=title)
        student = Student.objects.get(roll_number=roll_number)
        book.borrowed_by.add(student)
        student.books_taken.add(book)
        return redirect('view_books')
    books = Book.objects.all()
    students = Student.objects.all()
    return render(request, 'issuebook.html', {'books': books, 'students': students})
def add_student(request):
    if request.method == "POST":
        roll_number = request.POST["roll_number"]
        name = request.POST["name"]
        student = Student(roll_number=roll_number, name=name)
        student.save()
        return redirect('view_students')
    return render(request, 'addstudent.html')
def edit_student(request, roll_number):
    student = Student.objects.get(roll_number=roll_number)
    if request.method == "POST":
        student.name = request.POST["name"]
        student.save()
        return redirect('view_students')
    return render(request, 'editstudent.html', {'student': student})
def view_students(request):
    students = Student.objects.all()
    return render(request, 'viewstudents.html', {'students': students})

def logout_view(request):
    logout(request)
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

