from django.urls import path
from groups import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('new/', views.GroupCreateView.as_view(), name='group_form'),
    path('posts/in/<slug>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('join/<slug>/', views.join_group, name='join_group'),
    path('leave/<slug>/', views.leave_group, name='leave_group'),
]
