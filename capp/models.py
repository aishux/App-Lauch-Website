from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    #instead of object names we'll see client names
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)
    img = models.ImageField(upload_to='assets/images')
    post_img = models.ImageField(upload_to='assets/images')

    #instead of object names we'll see client names
    def __str__(self):
        return self.title + ' by ' + self.author