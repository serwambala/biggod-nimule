from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('church/', views.church, name='church'),
    path('children/', views.children, name='children'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission, name='mission'),
    path('vision/', views.vision, name='vision'),
    path('story/', views.story, name='story'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]