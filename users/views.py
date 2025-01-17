from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Product,Cart,Category,User,Seller,Client
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,ProfileForm,RegisterForm,RegisterForm2
from django.db.models import Q
from .permissionmixin import AdminRequiredMixin


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'client/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

        form = LoginForm()
        return render(request, 'client/login.html', {'form': form})

class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'client/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'client':
                newstudent = Client()
                newstudent.user = user  
                newstudent.save()

            elif user.user_role == 'seller':
                newteacher = Seller()
                newteacher.user = user
                newteacher.save()


            return redirect('/dashboard')

        return render(request, 'client/register.html', {'form': form})

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/")

class ClientProduct(View):
    def get(self,request):
        search_query = request.GET.get('search', '')
        if search_query:
            products = Product.objects.filter(name__icontains=search_query)
        else:
            products = Product.objects.all()
        cart = Cart.objects.count()
        cotegory = Category.objects.all()
        return render(request,'client/home.html',{'products':products,'cart':cart, 'cotegory':cotegory})

class ClientCategory(View):
    def get(self,request,id):
        cotegory = Category.objects.all()
        cart = get_object_or_404(Category,id=id)
        products = cart.products.all()
        return render(request,'client/home.html',{'products':products, 'cotegory':cotegory})

class DetailView(View):
    def get(self,request,id):
        product = get_object_or_404(Product,id=id)
        cart = Cart.objects.count()
        return render(request,'client/batafsil.html',{'product':product,'cart':cart})
    
    def post(self,request,id):
        product = get_object_or_404(Product,id=id)
        quontity = int(request.POST['cart'])
        if Cart.objects.filter(product=product).exists():
            cart = Cart.objects.filter(product=product).first()
            cart.quontity += quontity
            cart.save()

        else:
            cart = Cart()
            cart.product=product
            cart.quontity=quontity
            cart.save()
        return redirect('/')
    
class Categories(View):
    def get(self,request,id):
        categor = get_object_or_404(Category,id=id)
        products = categor.products.all()
        return render(request,'client/home.html',{"products":products,'cats':categor})
    
class CartDetailView(View):
    def get(self,request):
        products = Cart.objects.all()
        return render(request,'client/cart.html',{"products":products}) 

def delete(request,id):
    cart = get_object_or_404(Cart,id=id)
    cart.delete()
    return redirect('/')


class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'client/profil.html',context={"user":user})
    
class EditProfileView(LoginRequiredMixin, View):
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
    
def seller(request):
    seller = User.objects.all()
    return render(request,'client/seller.html',{'seller':seller})

def client(request):
    client = Client.objects.all()
    return render(request,'client/client.html',{'client':client})


class Delete(AdminRequiredMixin,View):
    def get(self,request,id):
        client = get_object_or_404(Client, id=id)
        user = User.objects.get(username=client.user.username)
        client.delete()
        user.delete()
        return redirect('/dashboard')

    
def delete_user(request,id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('/dashboard')

class ProfileViewAdmin(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'client/dashboard.html',context={"user":user})
    

class RegisterView2( View):

    def get(self, request):
        form = RegisterForm2()
        return render(request, 'client/register2.html', {'form': form})

    def post(self, request):
        form = RegisterForm2(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            return redirect('/')

        return render(request, 'client/register2.html', {'form': form})