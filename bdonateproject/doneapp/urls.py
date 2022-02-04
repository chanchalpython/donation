from . import views

from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('donate',views.donate,name='donate'),
    path('logout',views.logout,name='logout'),
    path('fillform',views.fillform,name='fillform'),
    path('', views.PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', views.PersonUpdateView.as_view(), name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]
