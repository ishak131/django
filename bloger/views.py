import math
from django.conf import settings
from django.shortcuts import redirect, render
from bloger.models import Brand, CartProduct, Category, Product

def home_page(request):
    featured_product = Product.objects.all()[:9]
    return render(request, 'index.html', {"featured_product": featured_product})


def about_us(request):
    return render(request, 'about.html')


def addProductToCart(request, product_id, quantity):
    selected_product = Product.objects.get(id=product_id)
    cart_product = CartProduct(
        product=selected_product, productQuantity=int(quantity))
    cart_product.save()
    return render(request, 'close-window.html')


def removeProductToCart(request, product_id):
    instance = CartProduct.objects.get(id=product_id) 
    instance.delete()
    return render(request, 'close-window.html')

def cart(request):
    return render(request,'cart.html')

def shop_with_index(request, start_index, end_index):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products = Product.objects.all()[start_index:end_index]
    products_length = Product.objects.all().count()
    base_url = "shop.html"
    return render(request, 'shop.html', {
        "products": products,
        "categories": categories,
        "brands": brands,
        "base_url": base_url,
        "start_index": start_index,
        "products_length": range(math.ceil(products_length/9)),
    })


def shop(request):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products = Product.objects.all()[:9]
    products_length = Product.objects.all().count()
    base_url = "shop.html"
    return render(request, 'shop.html', {
        "products": products,
        "categories": categories,
        "brands": brands,
        "base_url": base_url,
        "products_length": range(math.ceil(products_length/9))
    })


def shop_with_a_specfic_category(request, product_category):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products_length = Product.objects.filter(category=product_category).count()
    products = Product.objects.filter(category=product_category)[:9]
    base_url = "shop.html/"+product_category
    return render(request, 'shop.html',
                  {
                      "products": products,
                      "categories": categories,
                      "brands": brands,
                      "base_url": base_url,
                      "products_length": range(math.ceil(products_length/9))
                  })


def shop_with_a_specfic_brand(request, product_brand):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products_length = Product.objects.filter(brand=product_brand).count()
    products = Product.objects.filter(brand=product_brand)[:9]
    base_url = "shop.html/brand/"+product_brand
    return render(request, 'shop.html',
                  {
                      "products": products,
                      "categories": categories,
                      "brands": brands,
                      "base_url": base_url,
                      "products_length": range(math.ceil(products_length/9))
                  })


def shop_with_a_specfic_category_with_index(request, product_category, start_index, end_index):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products_length = Product.objects.filter(category=product_category).count()
    products = Product.objects.filter(category=product_category)[
        start_index:end_index]
    base_url = "shop.html/"+product_category
    return render(request, 'shop.html',
                  {
                      "products": products,
                      "categories": categories,
                      "brands": brands,
                      "base_url": base_url,
                      "start_index": start_index,
                      "products_length": range(math.ceil(products_length/9))
                  })


def shop_with_a_specfic_brand_with_index(request, product_brand, start_index, end_index):
    categories = Category.objects.all()[:20]
    brands = Brand.objects.all()[:20]
    products_length = Product.objects.filter(brand=product_brand).count()
    products = Product.objects.filter(brand=product_brand)[
        start_index:end_index]
    base_url = "shop.html/brand/"+product_brand
    return render(request, 'shop.html',
                  {
                      "products": products,
                      "categories": categories,
                      "brands": brands,
                      "base_url": base_url,
                      "start_index": start_index,
                      "products_length": range(math.ceil(products_length/9))
                  })


def single_shop(request, product_id):
    product = Product.objects.get(id=product_id)
    related_product = Product.objects.filter(
        category=product.category).exclude(id=product_id)[:15]
    return render(request, 'shop-single.html',
                  {
                      "product": product,
                      "related_product": related_product,
                  })


# Create your custom error here.
def custom_page_not_found_view(request, exception):
    response = redirect('/EN')
    return response


def custom_error_view(request, exception=None):
    response = redirect('/EN')
    return response


def custom_permission_denied_view(request, exception=None):
    response = redirect('/EN')
    return response


def custom_bad_request_view(request, exception=None):
    response = redirect('/EN')
    return response
