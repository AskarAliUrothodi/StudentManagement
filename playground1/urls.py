"""
URL configuration for playground1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from poll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('Persons/', views.Persons),
    path('Persons/persondetails/<int:id>/', views.persondetails),
    path('addperson/', views.addperson),
    path('addperson/addpersonpageprocess/', views.addpersonpageprocess),
    path('Persons/persondetails/<int:id>/delete/', views.deleteperson),
    path('Persons/persondetails/<int:id>/updatepage/', views.updateperson),
    path('Persons/persondetails/<int:id>/updatepage/updatepageprocess/', views.updatepersonprocess),

    path('', views.login,name="loginpage"),
    path('authenticating/', views.authenticating),
    path('signup/', views.signup),
    path('signup/createaccount/', views.signpage),
    path('studentaddedsuccessful/', views.studentaddedsuccessful),
    path('updatestudent/', views.updatestudent),
    
    
    
    
    
    path('new/', views.new,name="homepage"),
    path('login1/', views.login1),
    path('addstudent/', views.addstudent),
    path('addstudentprocess/', views.addstudentprocess),
    path('featured_listings/',views.featured_listings),
    path('featured_listings/updatestudent/<int:id>/', views.updatestudent),
    path('featured_listings/updatestudent/<int:id>/updateprocess/', views.updateprocess),
    path('featured_listings/updatestudent/<int:id>/delete/', views.deletestudent),
    


  


   
   
]
