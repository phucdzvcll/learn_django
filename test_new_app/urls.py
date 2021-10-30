from django.urls import path

from . import views

app_name = 'test'
urlpatterns = [
    path('request/', views.testRequets, name='testRequets'),
    path('request/tesdfsddfgsdggfdfst/<int:id>/', views.detail, name='result'),
    path('request/<int:id>/', views.detail, name='detail'),
]