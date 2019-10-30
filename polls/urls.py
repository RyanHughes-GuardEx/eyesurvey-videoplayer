from django.urls import path

from . import views

# here are the URL manager for requests to http:// ... /polls/*
app_name = 'polls'
urlpatterns = [
    path('<str:user_id>/vote/', views.vote, name='vote'),
    path('<str:user_id>-<str:video_num>/vote/submit', views.results, name='results'),
]
