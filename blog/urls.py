from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home_page'),

    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post_detail'),

    path('post/create/', views.PostCreateView.as_view(), name='post_create'),

    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),

    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('<str:username>/author/', views.UserPostListView.as_view(), name='user_post_list'),

    path('latest/posts/', views.latest_articles_view, name='latest_posts'),

    path('responsive/', views.responsive_view, name='responsive_page'),

    path('top-questions/', views.top_interview_questions_view,
         name='top_questions_page'),




    # path('', views.home_view, name='home_page'),
]