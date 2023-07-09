from django.urls import path
from django.contrib.auth import views as auth_views

from usersapp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
    path('patient_texts/<str:username>/', views.patient_texts, name='patient_texts'),
    path('patient_infos/<str:username>/', views.patient_info, name='patient_infos'),
    path('update_patient_left/<str:username>/', views.update_patient_left, name='update_patient_left'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='usersapp/password_reset.html'), name = 'password_reset'),
	# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='usersapp/password_reset_done.html'), name='password_reset_done'),
	# path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='usersapp/password_reset_confirm.html'), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='usersapp/password_reset_complete.html'), name='password_reset_complete'),
    path('profil/', views.profil, name='profil'),
    path('create_patient/', views.create_patient, name='create_patient'),
    path('patient_credentials/<str:username>/<str:password>/<str:email>/', views.patient_credentials, name='patient_credentials'),
    # path('change_password/', views.change_password, name='change_password'),
    path('patient_list/', views.patient_list, name='patient_list'),

]