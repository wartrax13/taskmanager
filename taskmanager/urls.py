from django.contrib import admin
from taskmanager.item import views

from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name='home'),
]
