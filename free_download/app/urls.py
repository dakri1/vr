from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', ProgramsHome.as_view(), name="home"),
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logoutUser, name='logout'),
    path('post/<slug:post_slug>/', ProgramPost.as_view(), name='show_post'),
    path('category/<slug:cat_slug>/', ProgramsCategory.as_view(), name='category'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete")

]

