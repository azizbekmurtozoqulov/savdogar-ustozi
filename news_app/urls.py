from django.urls import path, include
from . import views
from .views import homePageView

from django.urls import path
from . import views

urlpatterns = [

    path('', views.homePageView, name='home_page'),
    path('home/', views.index, name='home'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),

]
