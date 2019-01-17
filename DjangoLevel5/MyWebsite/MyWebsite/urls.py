
from django.contrib import admin
from django.urls import path,include
from basicApp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('basicApp/',include('basicApp.urls')),
    path('admin/', admin.site.urls),
    path('logout/', views.user_logout,name='logout'),
    # path('') 
]
