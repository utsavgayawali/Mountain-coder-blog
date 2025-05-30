from django.shortcuts import render
from home.models import Blog
from home.models import Carousel,Contact
import math

def home(request):
    image = Carousel.objects.all()
    context ={'images':image}
    return render(request,'home.html',context)
def blog(request):
     no_of_post=4
     page= request.GET.get('page')
     if page is None:
         page=1
     else:
         page=int(page)
 
    
     all_data = Blog.objects.all()
     all_data=all_data[(page-1)* no_of_post:no_of_post+(page-1)* no_of_post]
     prev=None
     if page>=1:
         prev=page-1
     else:
         pre=None
     nxt=None
     if page< math.ceil( Blog.objects.count()/no_of_post):
         nxt=page+1
     else:
         nxt=None
    
         
     context ={'items':all_data,'prev':prev,'nxt':nxt}
     return render(request,'blog.html',context)


    



def contact(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        description=request.POST['description']
        instance = Contact(name=name,email=email,phone=phone,description=description)
        instance.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def search(request):
    return render(request,'search.html')

def blogpost(request,slug):
    all_data = Blog.objects.filter(slug=slug).first()
    context={'items':all_data}
    return render(request,'blogpost.html',context)
