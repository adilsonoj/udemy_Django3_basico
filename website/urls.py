from django.urls import path, include
from .views import hello_blog
from .views import post_details, save_form

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_details, name='post_details'),
    path('save_form', save_form, name='save_form')
]
