from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Product


def index(request):
    return HttpResponse('<h1>Hello</h1>')


class HomePageView(generic.TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context={'data': Product.objects.all()})
    
    