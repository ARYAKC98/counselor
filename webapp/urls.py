from django.urls import path
from webapp import views

urlpatterns=[
    path('home_page/', views.home_page, name='home_page'),
    path('register_page/', views.register_page, name='register_page'),
    path('about_page/', views.about_page, name='about_page'),
    path('counselor_page/', views.counselor_page, name='counselor_page'),
    path('service_page/', views.service_page, name='service_page'),
    path('price_page/', views.price_page, name='price_page'),
    path('blog_page/', views.blog_page, name='blog_page'),
    path('contact_page/', views.contact_page, name='contact_page'),
    path('single_page/', views.single_page, name='single_page'),

]