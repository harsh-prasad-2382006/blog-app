"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('create-post/',views.create_post,name='create-post'),
    path('edit-post/<int:id>/',views.edit_post,name='edit-post'),
    path('delete-post/<int:id>/',views.delete_post,name='delete-post'), 
    path('read-more/<int:id>/',views.read_more,name='read-more'), 
    path('pricing/', views.pricing_view, name='pricing'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('payment/payment-success/',views.payment_success,name='payment-success'),
]
