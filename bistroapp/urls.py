from django.urls import  path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('service/',views.service,name='service'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('clients/',views.clients,name='clients'),
    path('menu/',views.menu,name='menu'),
    path('booking/',views.booking,name='booking'),
    path('chef/',views.chef,name='chef'),
    path('condition/',views.condition,name='condition'),
    path('privacy/',views.privacy,name='privacy'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('addmenu/',views.addmenu,name='addmenu'),
    path('addchef/',views.addchef,name='addchef'),
    path('bistromenu/',views.bistromenu,name='bistromenu'),
    


    



]