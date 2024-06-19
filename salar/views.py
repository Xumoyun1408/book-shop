from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from  users.permissionmixin import SellerRequiredMixin
from  django.views import  View
from .forms import ProductForm
from django.urls import reverse
from users.models import Product,Client,User
from users.forms import ResetPasswordForm,ProfileForm

class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'seller/products.html', {'products': products})

    
class ProfileViewAdmin(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'seller/dashboard.html',context={"user":user})

class Delete(LoginRequiredMixin, View):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect('/dashboard')
    
class CreateProductView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'seller/create.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('seller:dashboard')
        return render(request, 'seller/create.html', {'form': form})
    
class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = get_object_or_404(Product,id=id)
        form = ProductForm(instance=product)
        return render(request, 'seller/update.html', {'form': form})

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller:dashboard')  
        return render(request, 'seller/update.html', {'form': form})
    
class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'seller/profil.html',context={"user":user})
    


class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm()
        return render(request, 'seller/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('seller/dashboard')
        form = ResetPasswordForm()
        return render(request, 'seller/reset_password.html', {'form':form})
    
class EditProfileViewSeller(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'client/edit.html', {'form': form})
    
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profil')
        return render(request, 'client/edit.html', {'form': form})
    