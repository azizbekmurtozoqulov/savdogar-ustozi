

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from news_app import views
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('contact')),
    path('', views.index, name='contact'),
    path('news/', include('news_app.urls')),  # bo'sh path o‘rniga prefix qo‘yildi
    path('contact/', views.contact, name='contact'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)