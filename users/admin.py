from django.contrib import admin
from .models import User,Cart,Category,Product,Seller,Client

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Seller)