from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.homeb, name='homeb'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('todo/',views.add_show, name='addandshow'),
    path('delete/<int:id>',views.delete_data, name='deletedata'),
    path('<int:id>/',views.update_data, name='updatedata'),
]