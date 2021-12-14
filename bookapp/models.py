from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self) -> str:
        return self.full_name

class Book(models.Model):    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    stock = models.IntegerField(default=0)
	