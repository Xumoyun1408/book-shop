from django.urls import path
from .views import ProductsView,ProfileViewAdmin,Delete,CreateProductView,EditProfileView,ProfileView,ResetPasswordView,EditProfileViewSeller

app_name = 'seller'

urlpatterns = [
    path('products/',ProductsView.as_view(),name='products'),
    path('seller/delete/<int:id>/',Delete.as_view(),name='delete'),
    path('seller/update/<int:id>/', EditProfileView.as_view(), name='update'),
    path('seller/edit/<int:id>/', EditProfileViewSeller.as_view(), name='edit'),
    path('products/create/', CreateProductView.as_view(), name='create_product'),
    path('dashboard/',ProfileViewAdmin.as_view(),name='dashboard'),
    path('resed-password/',ResetPasswordView.as_view(),name='resed_password'),
    path('profil/',ProfileView.as_view(),name='profil'),
]