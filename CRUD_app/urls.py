from django.urls import include, path
from .import views

app_name = 'CRUD_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.create_user, name='signup'),
    path('signin/', views.sign_in, name='signin'),
    path('signout/', views.sign_out, name='signout'),
    path('delete/<int:id>/', views.delete_user, name='deleteUser'),
    path('edit/<int:id>/', views.edit_user, name='editUser'),

]
