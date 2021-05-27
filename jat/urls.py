from django.urls import path

from jat import views

app_name = 'jat'

urlpatterns = [
    path('', views.RepositoryListView.as_view(), name='repository_list'), #jat:repository_list -> path의 풀네임
    path('repository/<int:pk>/', views.RepositoryDetailView.as_view(), name='repository_detail'),
]
