from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
 
class Post( models.Model ):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) 
    #www.pytnotes.com/blo;introducao-ao-python essa e a forma que eu vou armazenar cada dado via web 
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("note:detail", kwargs={"slug":self.slug})