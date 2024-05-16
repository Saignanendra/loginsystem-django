from django.db import models


#path for user uploaded profile images
def user_directory_path(instance, filename):
    # Media file upload path: media/<user_id>/profileimage/<filename>
    return f'static/media/{instance.id}/profileimage/{filename}' 

    
# Create your models here.
class User1(models.Model):
    objects = None
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=250, verbose_name="Student Email")


    def __str__(self):
        return str(self.id)
    

class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    image= models.ImageField(upload_to=user_directory_path, null=True)
    


    def __str__(self):
        return self.title
