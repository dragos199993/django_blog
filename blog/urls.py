from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="blog_list"),
    path('<int:pk>', views.detail, name="blog_detail"),
]
