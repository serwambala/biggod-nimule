from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('church/', views.church, name='church'),
    path('children/', views.children, name='children'),
    path('get-involved/', views.get_involved, name='get_involved'),
    path('about/', views.about, name='about'),
    path('core-values/', views.core_values, name='core-values'),
    path('vision/', views.vision, name='vision_&_mission'),
    path('story/', views.story, name='story'),
    path('give/', views.give, name='give'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('statement-of-faith/', views.statement_of_faith, name='statement-of-faith'),
    path('leadership/', views.leadership, name='leadership'),
    path('sermon/<int:id>/', views.sermon_detail, name='sermon_detail'),
]