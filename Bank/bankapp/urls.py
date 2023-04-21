from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
app_name='bankapp'
urlpatterns = [

    path('',views.index,name='index'),
    # path('profile',views.profile,name='profile'),
    path('newpage',views.newpage,name='newpage'),




    path('add_person', views.person, name="person"),
    path('branch', views.branch, name="branch")
    # path('add',views.add,name='add'),
    #
    # path('profilecreateview',views.PersonCreateView.as_view(),name='profilecreateview'),
    #
    # path('getstate',views.getstate,name='getstate'),
    # path('getdist',views.getdist,name='getdist'),
    # path('getbranch',views.getbranch,name='getbranch')
    #
    #

]

