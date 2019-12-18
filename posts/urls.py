from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.index, name='index'),
    path('post/<int:postnum>', views.details, name='details')
]
