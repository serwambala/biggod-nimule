from django.contrib import admin

# Register your models here.

from .models import ContactMessage

admin.site.register(ContactMessage)

from django.contrib import admin

from .models import (
    Sermon,
    Event,
    Testimony
)



@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'created_at'
    )

    search_fields = (
        'title',
    )



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'date',
        'location'
    )



@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'approved',
        'created_at'
    )

    list_filter = (
        'approved',
    )

    search_fields = (
        'name',
        'message'
    )