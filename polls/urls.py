from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('<str:user_id>/vote/', views.vote, name='vote'),
]
