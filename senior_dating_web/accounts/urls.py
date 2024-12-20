from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from .views import send_confirmation_email
from .views import delete_account, confirm_delete_account  # Import the view here
from .views import reset_password, forgot_password



urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('register/', views.register, name='register'),
    path('matches/', views.find_matches, name='find_matches'),
    path('send_message/<int:user_id>/', views.send_message, name='send_message'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('main/', views.main_page, name='main_page'),
    path('delete_account/', views.delete_account, name='delete_account'),  # URL to delete account
    path('update_bio/', views.update_bio, name='update_bio'),  # URL to update bio
    path('update_profile_image/', views.update_profile_image, name='update_profile_image'),  # URL to update profile image
    path('add_friend/<int:user_id>/', views.add_friend, name='add_friend'),  # URL to add a friend
    path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),  # URL to send friend request
    path('accept_friend_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),  # URL to accept friend request
    path('decline_friend_request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),  # URL to decline friend request
    path('remove_friend/<int:user_id>/', views.remove_friend, name='remove_friend'),  # URL to remove a friend
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', reset_password, name='reset_password'),


    # Password Reset URLs (using Django's built-in views)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Account Deletion Confirmation
    path('confirm-delete/<int:user_id>/', confirm_delete_account , name='confirm_delete'),  # Clearer naming for account deletion
    path('send_confirmation_email/', send_confirmation_email, name='send_confirmation_email'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
