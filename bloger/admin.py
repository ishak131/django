from django.contrib import admin

from .models import Brand, CartProduct, Category,Product,Size,Color

admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(CartProduct)
# Register your models here.
