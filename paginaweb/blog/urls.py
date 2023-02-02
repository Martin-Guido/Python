
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.blog, name='blog'),
    path('categoria/<int:cat_id>/',views.categoria, name='categoria'),

   ]