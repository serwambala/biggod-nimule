
from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def church(request):
    return render(request, 'pages/church.html')

def children(request):
    return render(request, 'pages/children.html')

def get_involved(request):
    return render(request, 'pages/get_involved.html')

def about(request):
    return render(request, 'pages/about.html')

def story(request):
    return render(request, 'pages/story.html')

def vision(request):
    return render(request, 'pages/vision.html')

def core_values(request):
    return render(request, 'pages/core-values.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def leadership(request):
    return render(request, 'pages/leadership.html')

def statement_of_faith(request):
    return render(request, 'pages/statement-of-faith.html')


from django.http import HttpResponse
from .models import ContactMessage

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return HttpResponse("Message received. Thank you for contacting us.")

    return render(request, "pages/contact.html")

from django.shortcuts import render, redirect

from .models import (
    Event,
    Testimony,
    Sermon
)


def church(request):

    # HANDLE TESTIMONY SUBMISSION
    if request.method == 'POST':

        name = request.POST.get('name')

        message = request.POST.get('message')

        Testimony.objects.create(
            name=name,
            message=message
        )

        return redirect('church')


    # GET MOST RECENT SERMON
    latest_sermon = Sermon.objects.order_by('-created_at').first()

    # GET EVENTS
    events = Event.objects.all().order_by('date')


    # GET APPROVED TESTIMONIES
    testimonies = Testimony.objects.filter(
        approved=True
    ).order_by('-created_at')[:5]


    context = {
        'latest_sermon': latest_sermon,
        'events': events,
        'testimonies': testimonies,
    }

    return render(
        request,
        'pages/church.html',
        context
    )
def sermon_detail(request, id):
    sermon = Sermon.objects.get(id=id)
    return render(request, 'sermon_detail.html', {'sermon': sermon})

from .models import Sermon


def home(request):
    latest_sermon = Sermon.objects.first()

    context = {
        'latest_sermon': latest_sermon
    }

    return render(request, 'pages/home.html', context)




from django.shortcuts import render
from .models import ChildProfile


def children(request):

    children_profiles = ChildProfile.objects.all()

    featured_children = ChildProfile.objects.filter(
        featured=True
    )[:3]

    context = {
        "children_profiles": children_profiles,
        "featured_children": featured_children,
    }

    return render(
        request,
        "pages/children.html",
        context
    )