from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('list', views.list_work, name='list'),
    path('login', views.login_in, name='login'),
    path('logout', views.logout_user, name='logout')
]
