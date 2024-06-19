from django.urls import path
from .views import ClientProduct,DetailView,Categories,CartDetailView,delete,LoginView,ClientCategory,ProfileView,EditProfileView,LogoutView,RegisterView,seller,ProfileViewAdmin,client,Delete,RegisterView2, delete_user

app_name = 'client'

urlpatterns = [

   
    path('login/',LoginView.as_view(),name='login'),
    path('',ClientProduct.as_view(),name='products'),
    path('batafsil/<int:id>/',DetailView.as_view(),name='batafsil'),
    path('cart/',DetailView.as_view(),name='cart'),
    path('carts/',CartDetailView.as_view(),name='carts'),
    path('categories/<int:id>/',Categories.as_view(),name='categories'),
    path('delete/<int:id>/',delete,name='delete'),
    path('deletec/<int:id>/',Delete.as_view(),name='deletec'),
    path('category/<int:id>/',ClientCategory.as_view(),name='categor'),
    path('edit/<int:id>/',EditProfileView.as_view(),name='edit'),
    path('profil/',ProfileView.as_view(),name='profil'),
    path('dashboard/',ProfileViewAdmin.as_view(),name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register2/', RegisterView2.as_view(), name='register2'),
    path('seller/',seller, name='seller'),
    path('client/',client, name='client'),
    path('delete-user/<int:id>/', delete_user, name="delete_user"),



]