from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import DashboardView, SignInView, SignOutView, SignUpView, ChangePasswordView, ChangeUserData, DeleteUserView, ResetPasswordView

app_name = "sevo_user"
urlpatterns = [
    #path("", index, name="index"),
    path("dashboard/", DashboardView.as_view(), name="index"),

    path("sign-up/", SignUpView.as_view(), name="sign_up"),

    path("sign-in/", SignInView.as_view(), name="sign_in"), 

    path("sign-out/", SignOutView.as_view(), name="sign_out"),

    path("password-change", ChangePasswordView.as_view(), name="password_change"), 
    path("userdata-change/<int:pk>", ChangeUserData.as_view(), name="update"),
    path("user-delete/<int:pk>", DeleteUserView.as_view(), name="delete"),
    path("password-reset/", ResetPasswordView.as_view(), name="password_reset"),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='sevo_user/password_reset_confirm.html', success_url=reverse_lazy("sevo_user:password_reset_complete")), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='sevo_user/password_reset_complete.html'), name='password_reset_complete'),

]

# https://dev.to/earthcomfy/django-reset-password-3k0l
