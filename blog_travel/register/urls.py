from django.contrib.auth.views import LogoutView
from django.urls import path

import register.views as register

app_name = 'register'

urlpatterns = [
    path('',
         register.signup,
         name='user_create'),
    path('login/',
         register.log_in,
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
    path('profile/<username>/',
         register.profile,
         name='profile')
    # path('password_reset/', PasswordResetView.as_view(
    #     template_name='register/password_reset.html',
    #     email_template_name='users/password_reset_email.html',
    #     subject_template_name='users/password_reset_subject.txt',
    #     success_url='/users/password_reset/done/'),
    #      name='password_reset'
    #      ),
    # path('password_reset/done/', PasswordResetDoneView.as_view(
    #     template_name='register/password_reset_done.html'),
    #      name='password_reset_done'
    #      ),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
    #     template_name='register/password_reset_confirm.html',
    #     success_url='/users/reset/done/'),
    #      name='password_reset_confirm'
    #      ),
    # path('reset/done/', PasswordResetCompleteView.as_view(
    #     template_name='register/password_reset_complete.html'),
    #      name='password_reset_complete'
    #      ),

]
