"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

# from apartments.views import applicants
from apartments import views
from apartments.views import order

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", index, name="index"), 
    # path("", apartment, name="apartment"),
    path('', views.index, name="index"),
    # path("description", description, name="description"), 
    # path("applicants", applicants, name="applicants"), 
    path("order/<int:application_id>", views.order, name="order"), 
    path('apartments/<int:id_apartments>/', views.apartments_detail, name='apartments_detail'),

]
