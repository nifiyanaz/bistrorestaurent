
from django.shortcuts import redirect, render
from .models import Chef,Menu
from .forms import MenuForm,ChefForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def service(request):
    return render(request,'service.html') 
def contact(request):
    return render(request,'contact.html')  
def about(request):
    return render(request,'about.html')
def clients(request):
    return render(request,'clients.html') 
def pages(request):
    return render(request,'pages.html')
def booking(request):
    return render(request,'booking.html')

def condition(request):
    return render(request,'condition.html')

def testimonial(request):
    return render(request,'testimonial.html')


def privacy(request):
    return render(request,'privacy.html')

def bistromenu(request):
    return render(request,'bistromenu.html')

def menu(request):
    tasks=Menu.objects.all()
    return render(request,'menu.html',{'tasks':tasks})


def addmenu(request):    
    mform=MenuForm()
    if request.method=='POST':
       mform=MenuForm(request.POST,request.FILES)
       if mform.is_valid():
           mform.save()
           return redirect('menu')
       else:
           message=mform.errors
           mform=MenuForm()
           return render(request,'addmenu.html',{'form':mform,'msg':message})
    else:
        mform=MenuForm()
        return render(request,'addmenu.html',{'form':mform})


def chef(request):
    tasks=Chef.objects.all()
    return render(request,'chef.html',{'tasks':tasks})


def addchef(request):    
    form=ChefForm()
    if request.method=='POST':
       form=ChefForm(request.POST,request.FILES)
       if form.is_valid():
          form.save()
          return redirect('chef')
       else:
          print(form.errors)
          form=ChefForm()
          return render(request,'addchef.html',{'form':form})
    else:
        form=ChefForm()
        return render(request,'addchef.html',{'form':form})
  


    