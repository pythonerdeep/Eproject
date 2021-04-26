from django.urls import path
from .import views

urlpatterns=[
    path('s',views.sign),
    path('login/',views.login),
    path('dash',views.dashboard),
    path('logout',views.logout)
]