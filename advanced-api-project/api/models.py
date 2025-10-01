from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    published_year = models.IntegerField()

    def __str__(self):
        return self.title