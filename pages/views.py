
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

def mission(request):
    return render(request, 'mission.html')

def gallery(request):
    return render(request, 'gallery.html')


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