from django.contrib import admin
from .models import User1, Student, Task

# Register your models here.
@admin.register(User1)
class User1Admin(admin.ModelAdmin):
    list_display = ['id', 'username']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'name', 'email']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title']