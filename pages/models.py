from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
from django.db import models


class Sermon(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField()

    video = models.FileField(
        upload_to='sermons/videos/'
    )

    thumbnail = models.ImageField(
        upload_to='sermons/thumbnails/'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title



class Event(models.Model):
    title = models.CharField(max_length=200)

    date = models.DateField()

    location = models.CharField(max_length=200)

    description = models.TextField()

    def __str__(self):
        return self.title



class Testimony(models.Model):
    name = models.CharField(max_length=100)

    message = models.TextField()

    approved = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name