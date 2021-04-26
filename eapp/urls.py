from django.urls import path
from .import views

urlpatterns=[
    path('f',views.form),
    path('f2',views.form2),
    path('f3',views.form3),
    path('f4',views.form4),
    path('loc',views.location),
    path('f5',views.form5),
    path('login/',views.login),
    path('log',views.logout),
    path('otp',views.otp),
    path('v',views.verify),
    path('sub',views.submit)
]