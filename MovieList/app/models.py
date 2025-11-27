from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length= 255)
    director = models.CharField(max_length= 255)
    genre = models.CharField(max_length= 255)
    release_date = models.DateField()
    rating = models.FloatField()
    duration = models.DurationField(help_text="Duration (e.g. 2:29:00 or '2h 29m')")
    language = models.CharField(max_length= 255)
    description = models.TextField()
    watched = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title