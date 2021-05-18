from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Website_title(models.Model):
    teg                 =       models.CharField(max_length=500)


class Testimonial(models.Model):
    name                =       models.CharField(max_length=255)
    img                 =       models.ImageField(upload_to='media')
    prof                =       models.CharField(max_length=100)
    disc                =       models.CharField(max_length=500)
    social_link_f       =       models.URLField(default="facebook.com")
    social_link_t       =       models.URLField(default="twiter.com")
    social_link_i       =       models.URLField(default="instagram.com")
    social_link_l       =       models.URLField(default="linkedin.com")

    def __str__(self):
        return self.name

class Photo(models.Model):
    photo           =       models.ImageField(upload_to='media') 
    field           =       models.CharField(max_length=255)

    def __str__(self):
        return self.field

SUBJECT_CHOICES = [
    ('Maths', 'Maths'),
    ('Science', 'Science'),
    ('Social', 'Social'),
    ('English', 'English'),
    ('Computer', 'Computer'),
]

class Course(models.Model):
    subject         =       models.CharField(max_length=255, choices=SUBJECT_CHOICES, default='Maths')
    topic           =       models.CharField(max_length=255)
    img             =       models.ImageField(upload_to="media")
    disc            =       RichTextField()

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        return reverse("topic",kwargs={
            "pk":self.pk
        })

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Services(models.Model):
    symbol = models.CharField(max_length=255 ,blank=True)
    name = models.CharField(max_length=500)
    dics = RichTextField()

  
