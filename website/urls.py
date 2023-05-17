from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    # path('404/', views.errorpage, name='404'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('achivements/', views.achivements, name='achivements'),
    path('blog/', views.blog, name='blog'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery2/', views.gallery2, name='gallery2'),
    path('blogDetails/', views.blogDetails, name='blogDetails'),
    path('clubHistory/', views.clubHistory, name='clubHistory'),

    #Auth Urls
    path('user_login/', views.user_login, name='user_login'),
    path('user_register/', views.user_register, name='user_register'),

]