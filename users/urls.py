from django.urls import  path

from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', user_views.register_view, name='register_page'),

    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login_page'),

    path('logout/', user_views.logout_view, name='logout_page'),

    path('profile/', user_views.profile, name='profile_page'),

]