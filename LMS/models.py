from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    books_taken = models.ManyToManyField('Book', blank=True, related_name='students_taken')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    price = models.IntegerField()
    borrowed_by = models.ManyToManyField(Student, blank=True, related_name='books_borrowed')

    def __str__(self):
        return self.title
