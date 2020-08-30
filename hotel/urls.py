from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [

    path('home/',views.home,name='home'),
    path('list/',views.list,name='list'),
    path('vacatedrnac/<id>',views.vacatedrnac,name='vacatedrnac'),
    path('bookedrnac/<id>',views.bookedrnac,name='bookedrnac'),
    path('vacatedrac/<id>',views.vacatedrac,name='vacatedrac'),
    path('bookedrac/<id>',views.bookedrac,name='bookedrac'),
    path('vacateddac/<id>',views.vacateddac,name='vacateddac'),
    path('bookeddac/<id>',views.bookeddac,name='bookeddac'),

]
