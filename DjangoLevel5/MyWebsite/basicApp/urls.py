# from django.conf.urls import url
from django.urls import path
from basicApp import views

# Template URLS!
app_name = 'basicApp'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')

]