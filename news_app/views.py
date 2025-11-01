from gc import get_objects

from django.shortcuts import render, redirect, get_object_or_404
from unicodedata import category

from news_app.models import News, Category, Contact



def index(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')

def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list,
    }
    return render(request, 'news_list.html', context)


def news_details(request, id):
    news =get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news': news,
    }
    return render(request, 'news/news_details.html', context)

def homePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/home.html', context)

def contact_view(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('contact')  # yoki contact sahifasiga qaytarish
    return render(request, 'contact.html')

# news_app/views.py

from django.shortcuts import render, redirect
from .forms import ResumeForm

def resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume')  # Yoki 'success' sahifaga yo‘naltiring
    else:
        form = ResumeForm()
    return render(request, 'resume.html', {'form': form})


