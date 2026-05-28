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

from django.contrib import admin
from .models import ChildProfile


@admin.register(ChildProfile)
class ChildProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "age",
        "gender",
        "sponsorship_level",
        "sponsorship_status",
        "featured",
    )

    list_filter = (
        "gender",
        "sponsorship_level",
        "sponsorship_status",
        "featured",
    )

    search_fields = (
        "name",
        "dream",
        "school",
    )

    list_editable = (
        "featured",
        "sponsorship_status",
    )

from django.contrib import admin
from .models import GivePartner


@admin.register(GivePartner)
class GivePartnerAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'phone',
        'purpose',
        'submitted_at'
    )

    search_fields = (
        'name',
        'phone',
        'email'
    )

    list_filter = (
        'purpose',
        'submitted_at'
    )