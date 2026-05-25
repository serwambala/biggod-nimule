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

    video_url = models.URLField(
        max_length=500,
        help_text="Paste YouTube, TikTok, Facebook, or any sermon video link."
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
    
from django.db import models


class SponsorshipOption(models.Model):
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ChildProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    image = models.ImageField(upload_to='children_profiles/')
    short_story = models.TextField()
    needs = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ChildrenProgram(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='children_programs/')
    description = models.TextField()

    def __str__(self):
        return self.title


class ImpactStory(models.Model):
    child_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='impact_stories/')
    testimony = models.TextField()

    def __str__(self):
        return self.child_name