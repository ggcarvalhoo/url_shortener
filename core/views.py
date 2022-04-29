from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import FormLinks
from .models import Links


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status': status})


def check_url(request, link):
    form = FormLinks(request.POST)

    url_shortener = form.data['url_shortener']
    links = Links.objects.filter(url_shortener=url_shortener)
    if len(links) > 0:
        return redirect("/?status=1")

    if form.is_valid():
        try:
            form.save()
            return HttpResponse(f"URL has been created succesfully and it's: http://127.0.0.1:8000/{form.data['url_shortener']}")
        except:
            return HttpResponse("Unexpected error, try again please")


def redirect(request, link):
    links = Links.objects.filter(url_shortener=link)
    if len(links) == 0:
        return redirect('/')
    print(links)
    return redirect(links[0].url)
