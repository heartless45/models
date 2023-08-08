from django.shortcuts import render
from .models import Article
# Create your views here.
def home(request):
    articles = Article.objects.all()

    return render(request ,'1.html',{'articles':articles})

def a(request):
    return render(request , '2.html')