from django.urls import path, include
from MinTest import views

urlpatterns = [
    path('index/', views.index),
    path('login/', views.login),
    path('registe_mail/', views.registe_mail),
    path('registe_sms/', views.registe_sms),
    path('userinform/',views.userinform),
    path('time/', views.time),
    path('admin_list/', views.admin_list),
    path('news_list/', views.news_list),
    # path('news_add/', views.news_add),
    # path("send_mail/", views.send_qqmail),
    # path("send_sms/", views.send_qqsms),
]