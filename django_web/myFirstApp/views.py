from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Product
from django.views import View
from django.views.generic import TemplateView, DetailView


class Index(TemplateView):
    template_name = 'myFirstApp/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

def index(request):
    products=Product.objects.all()
    return render(request,"myFirstApp/base.html",{'products':products})

class AboutView(Index):
    template_name = "myFirstApp/about.html"

class ProductDetail(DetailView):
    template_name = 'myFirstApp/detail.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

def detail(request, product_id):
    product=Product.objects.get(id=product_id)
    return render(request,"myFirstApp/detail.html",{'product':product})

def test(request):
    return render(request,"test.html")