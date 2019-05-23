"""my_first_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from random import randint

def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)

def portfolio_page(request):
    image_urls = []
    for i in range(5):
        rand_num = randint(0, 100)
        image_urls.append(f"https://picsum.photos/400/600/?image={rand_num}")
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_page(request):
    context = {'skills': ['python', 'html', 'css', 'after effects', 'photoshop', 'premiere'], 'interests': ['Gunpla', 'Video Games', 'Podcasts', 'SciFi', 'Writing', 'Comics']}

    response = render(request, 'about.html', context)
    return HttpResponse(response)

urlpatterns = [
    path('home/', home_page),
    path('portfolio/', portfolio_page),
    path('about/', about_page)
]
