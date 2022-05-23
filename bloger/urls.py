from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.home_page, name='Home'),
    path('about.html', views.about_us, name='About'),
    path('shop.html', views.shop, name='shop'),
    path('shop.html/<int:start_index>/<int:end_index>',
         views.shop_with_index, name='shop'),
    path('shop.html/<str:product_category>',
         views.shop_with_a_specfic_category, name='shop-category'),
    path('shop.html/<str:product_category>/<int:start_index>/<int:end_index>',
         views.shop_with_a_specfic_category_with_index, name='shop-category'),
    path('shop.html/brand/<str:product_brand>',
         views.shop_with_a_specfic_brand, name='shop-brand'),
    path('shop.html/brand/<str:product_brand>/<int:start_index>/<int:end_index>',
         views.shop_with_a_specfic_brand_with_index, name='shop-brand'),
    path('shop-single.html/<int:product_id>', views.single_shop, name='shop'),
    path('add_product/<int:product_id>/<int:quantity>',
         views.addProductToCart, name='addProductToCart'),
    path('remove_product/<int:product_id>',
         views.removeProductToCart, name='remove_product'),
    path('cart',
         views.cart, name='cart'),
]
