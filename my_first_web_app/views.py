from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from random import randint

def root(request):
  return HttpResponseRedirect('home/')

def gallery(request):
  return HttpResponseRedirect('/portfolio')

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

def favourites_page(request):
    context = {'fave_links': ['https://bitmaker.co', 'https://www.vice.com/en_us/section/games', 'https://www.gundamkitscollection.com/']}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)