
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def church(request):
    return render(request, 'church.html')

def children(request):
    return render(request, 'children.html')

def get_involved(request):
    return render(request, 'get_involved.html')

def about(request):
    return render(request, 'about.html')

def story(request):
    return render(request, 'story.html')

def vision(request):
    return render(request, 'vision.html')

def core_values(request):
    return render(request, 'core-values.html')

def gallery(request):
    return render(request, 'gallery.html')

def leadership(request):
    return render(request, 'leadership.html')

def statement_of_faith(request):
    return render(request, 'statement-of-faith.html')


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

    return render(request, "contact.html")

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
    ).order_by('-created_at')[:3]


    context = {
        'latest_sermon': latest_sermon,
        'events': events,
        'testimonies': testimonies,
    }

    return render(
        request,
        'church.html',
        context
    )
def sermon_detail(request, id):
    sermon = Sermon.objects.get(id=id)
    return render(request, 'sermon_detail.html', {'sermon': sermon})