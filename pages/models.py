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


from django.db import models


class ChildProfile(models.Model):

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )

    SPONSORSHIP_CHOICES = (
        ("Bronze", "Bronze"),
        ("Silver", "Silver"),
        ("Gold", "Gold"),
    )

    STATUS_CHOICES = (
        ("Available", "Available"),
        ("Sponsored", "Sponsored"),
    )

    name = models.CharField(max_length=120)

    age = models.PositiveIntegerField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    image = models.ImageField(
        upload_to="children/",
        blank=True,
        null=True
    )

    story = models.TextField()

    dream = models.CharField(max_length=255)

    school = models.CharField(
        max_length=150,
        blank=True
    )

    favorite_subject = models.CharField(
        max_length=100,
        blank=True
    )

    sponsorship_level = models.CharField(
        max_length=20,
        choices=SPONSORSHIP_CHOICES,
        default="Bronze"
    )

    sponsorship_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Available"
    )

    needs = models.TextField(
        blank=True,
        help_text="School fees, clothing, food, medical support, etc."
    )

    scripture = models.CharField(
        max_length=255,
        blank=True
    )

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "name"]

    def __str__(self):
        return self.name



