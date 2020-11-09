from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('new/', views.PostCreateView.as_view(), name='post_form'),
    path('by/<str:username>/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('by/<str:username>', views.PostsByUserView.as_view(), name='posts_by_user'),
]
