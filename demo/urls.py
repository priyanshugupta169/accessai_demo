from django.urls import path
from . import views

# All the url patterns are listed here 
urlpatterns = [
   path('', views.login , name ='index'),
   path('index.html', views.index , name ='index'),
   path('register.html', views.register , name ='register'),
   path('logout.html', views.logout , name ='logout'),
   path('login.html', views.login , name ='login'),
   path('delete', views.delete , name ='delete'),
   path('update', views.update , name ='update'),
 ]